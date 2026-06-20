"""Helpers for exposing direct API media models in Streamlit pipeline UIs."""

import os
from typing import Any

import streamlit as st
from loguru import logger

from web.i18n import get_language


def is_api_workflow(workflow_key: str | None) -> bool:
    """Return True for direct provider workflow keys such as api/dashscope/xxx."""
    return bool(workflow_key and workflow_key.startswith("api/"))


def is_source_workflow(workflow: dict, source: str) -> bool:
    """Return True when a workflow belongs to a concrete source namespace."""
    key = workflow.get("key") or workflow.get("path") or ""
    return key.startswith(f"{source}/") or workflow.get("source") == source


def workflow_source_label(source: str) -> str:
    """Human-facing label for workflow source selectors."""
    from web.i18n import tr
    labels = {
        "selfhost": tr("api_workflows.source.selfhost"),
        "runninghub": "RunningHub",
        "api": tr("api_workflows.source.api"),
    }
    return labels.get(source, source)


def workflow_source_help(subject: str | None = None) -> str:
    """Common help text for workflow/model source selectors."""
    from web.i18n import tr
    subject_text = subject or tr("api_workflows.source_help_subject")
    return tr("api_workflows.source_help").replace("{subject}", subject_text)


def workflow_select_help() -> str:
    """Common help text for workflow/model select boxes."""
    from web.i18n import tr
    return tr("api_workflows.select_help")


def list_local_media_workflows(
    pixelle_video: Any,
    media_type: str,
    source: str,
    key_contains: str | None = None,
    key_prefix: str | None = None,
) -> list[dict]:
    """List non-API media workflows by source without mixing provider models."""
    try:
        workflows = []
        seen_keys = set()
        for workflow in pixelle_video.media.list_workflows():
            key = workflow.get("key") or workflow.get("path") or ""
            if not key or key.startswith("api/"):
                continue
            if not is_source_workflow(workflow, source):
                continue
            if key_contains and key_contains.lower() not in key.lower():
                continue
            if key_prefix:
                fname = os.path.basename(key)
                if not fname.startswith(key_prefix):
                    continue
            workflow_media_type = workflow.get("media_type")
            if media_type == "video":
                if workflow_media_type and workflow_media_type != "video":
                    continue
                if not workflow_media_type and "video_" not in key.lower() and not (key_prefix and os.path.basename(key).startswith(key_prefix)):
                    continue
            elif workflow_media_type and workflow_media_type != media_type:
                continue
            elif media_type == "image" and "video_" in key.lower():
                continue
            seen_keys.add(key)
            workflows.append({
                "key": key,
                "display_name": workflow.get("display_name") or key,
                **workflow,
            })

        if key_prefix:
            try:
                from pixelle_video.utils.os_util import get_resource_path, list_resource_files

                for filename in list_resource_files("workflows", source):
                    if not filename.startswith(key_prefix) or not filename.endswith(".json"):
                        continue
                    key = f"{source}/{filename}"
                    if key in seen_keys:
                        continue
                    seen_keys.add(key)
                    workflows.append({
                        "key": key,
                        "name": filename,
                        "display_name": f"{filename} - {source.title()}",
                        "source": source,
                        "path": get_resource_path("workflows", source, filename),
                        "media_type": media_type,
                    })
            except Exception as exc:
                logger.warning(f"Failed to list {source}/{key_prefix} workflows from files: {exc}")
        return workflows
    except Exception as exc:
        logger.warning(f"Failed to list {source} {media_type} workflows: {exc}")
        return []


def list_api_media_workflows(
    pixelle_video: Any,
    media_type: str,
    required_adapter_abilities: list[str] | tuple[str, ...] | set[str] | None = None,
    verified_only: bool = False,
) -> list[dict]:
    """List API-backed media workflows in the same option shape used by UIs."""
    api_media = getattr(pixelle_video, "api_media", None)
    if api_media is None:
        return []

    required = set(required_adapter_abilities or [])

    try:
        workflows = []
        for workflow in api_media.list_workflows():
            if workflow.get("media_type") != media_type:
                continue

            if verified_only and not workflow.get("api_contract_verified", True):
                continue

            adapter_abilities = set(workflow.get("adapter_ability_types") or [])
            if required and not required.intersection(adapter_abilities):
                continue

            workflows.append({
                "key": workflow["key"],
                "display_name": workflow.get("display_name") or workflow["key"],
                **workflow,
            })

        return workflows
    except Exception as exc:
        logger.warning(f"Failed to list API {media_type} workflows: {exc}")
        return []


def render_api_video_controls(
    workflow: dict | None,
    key_prefix: str,
    default_duration: int = 5,
    allow_audio_driven: bool = False,
    show_duration: bool = True,
    default_ratio: str | None = None,
) -> dict:
    """Render common API video controls based on verified adapter capability metadata."""
    from web.i18n import tr as _tr
    if not workflow or not is_api_workflow(workflow.get("key")):
        return {}

    capabilities = workflow.get("capabilities") or {}
    adapter_abilities = set(workflow.get("adapter_ability_types") or [])
    params: dict[str, Any] = {}

    with st.expander(_tr("api_workflows.api_video_title"), expanded=False):
        ability_text = ", ".join(sorted(adapter_abilities)) or _tr("api_workflows.unknown_ability")
        st.caption(_tr("api_workflows.adapter_abilities") + " " + ability_text)

        if not workflow.get("api_contract_verified", False):
            st.warning(_tr("api_workflows.contract_not_verified"))

        duration_contract = capabilities.get("duration") or {}
        min_duration = int(duration_contract.get("min", 3))
        max_duration = int(duration_contract.get("max", 15))
        if show_duration:
            default_value = min(max(int(default_duration or min_duration), min_duration), max_duration)
            params["duration"] = st.slider(
                _tr("api_workflows.duration"),
                min_value=min_duration,
                max_value=max_duration,
                value=default_value,
                step=1,
                key=f"{key_prefix}_api_duration",
            )
        else:
            st.caption(
                _tr("api_workflows.duration_follow_audio").replace("{min}", str(min_duration)).replace("{max}", str(max_duration))
            )

        resolutions = capabilities.get("resolutions") or []
        if resolutions:
            params["resolution"] = st.selectbox(
                _tr("api_workflows.resolution"),
                resolutions,
                index=0,
                key=f"{key_prefix}_api_resolution",
            )

        ratios = capabilities.get("ratios") or []
        if ratios:
            preferred_ratio = default_ratio or "9:16"
            default_ratio_index = ratios.index(preferred_ratio) if preferred_ratio in ratios else 0
            params["video_ratio"] = st.selectbox(
                _tr("api_workflows.aspect_ratio"),
                ratios,
                index=default_ratio_index,
                key=f"{key_prefix}_api_ratio",
            )

        negative_prompt = st.text_area(
            _tr("api_workflows.negative_prompt"),
            value="",
            height=70,
            key=f"{key_prefix}_api_negative_prompt",
        )
        if negative_prompt.strip():
            params["negative_prompt"] = negative_prompt.strip()

        if workflow.get("api_contract_verified", False):
            params["watermark"] = st.checkbox(
                _tr("api_workflows.watermark"),
                value=False,
                key=f"{key_prefix}_api_watermark",
            )

        if workflow.get("provider") == "seedance" and workflow.get("api_contract_verified", False):
            params["generate_audio"] = st.checkbox(
                _tr("api_workflows.generate_audio"),
                value=False,
                key=f"{key_prefix}_api_generate_audio",
            )

        if workflow.get("provider") == "kling" and workflow.get("api_contract_verified", False):
            params["sound"] = "on" if st.checkbox(
                _tr("api_workflows.generate_audio"),
                value=False,
                key=f"{key_prefix}_api_kling_sound",
            ) else "off"

        if allow_audio_driven and "audio_driven_i2v" in adapter_abilities:
            params["use_narration_audio_as_driving_audio"] = st.checkbox(
                _tr("api_workflows.audio_driven"),
                value=False,
                help=_tr("api_workflows.audio_driven_help"),
                key=f"{key_prefix}_api_audio_driven",
            )

    return {key: value for key, value in params.items() if value not in (None, "")}
