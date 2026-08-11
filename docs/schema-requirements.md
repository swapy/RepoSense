# Repo Sense Schema Requirements

This document defines the data schemas and structures for Repo Sense.
It focuses on the data contracts used by the website, prompt content, exports, and reports.

## Purpose

* Standardize the data shapes used across Repo Sense.
* Ensure consistent metadata and schema usage.
* Provide a reference for implementation and validation.

## Prompt metadata schema

Each prompt should follow a standard schema. Example fields:

* `id` (string)
* `name` (string)
* `description` (string)
* `pillar` (string)
* `capability` (string)
* `topic` (string)
* `use_cases` (array of strings)
* `automation_guidance` (string or array)
* `impact` (string)
* `best_practices` (array of strings)
* `applicable_languages` (array of strings)
* `tags` (array of strings)
* `confidence` (string)
* `status` (string)
* `severity` (string)
* `weight` (number)
* `coverage` (string or number)
* `evidence_requirements` (string)
* `related_prompts` (array of strings)
* `recommended_tools` (array of strings)
* `downloads` (integer)
* `created_at` (date)
* `updated_at` (date)
* `compliance_references` (array of strings)
* `validation_examples` (array of objects)
* `output_schema` (object or string)
* `component_types` (array of strings)

Controlled taxonomy fields should be validated against the shared Repo Sense vocabulary for pillars, capabilities, topics, languages, tools, and confidence levels.

## Ability page schema

Each Pillar, Capability, or Topic ability page should use a consistent schema for display, discovery, and automation guidance.
This schema is distinct from prompt metadata schema.

* `id` (string)
* `name` (string)
* `type` (string, e.g. `pillar`, `capability`, `topic`, `collective`)
* `summary` (string)
* `description` (string)
* `impact` (string)
* `use_cases` (array of strings)
* `automation_tools` (array of strings)
* `reference_links` (array of objects or strings)
* `pillar` (string)
* `capability` (string)
* `topic` (string)
* `related_abilities` (array of strings)
* `related_prompts` (array of strings)
* `tags` (array of strings)
* `updated_at` (date)
* `status` (string)
* `content` (string or rich text)

## Root manifest schema

The export bundle root manifest should specify:

* `bundle_name`
* `bundle_version`
* `selected_pillars`
* `selected_capabilities`
* `selected_topics`
* `prompt_files`
* `execution_order`
* `instructions`
* `metadata`
* `assessment_persona`
* `scope_rules`
* `validation_rules`

The root manifest schema is ready as the canonical orchestration contract for export bundles.
It should be used as the authoritative source for AI tool onboarding, prompt order, execution scope, and bundle validation.

## Report schema

Reports should use a consistent result schema:

* `repository_name`
* `repository_path`
* `generated_at`
* `scores`
  * `topic_scores`
  * `capability_scores`
  * `pillar_scores`
  * `global_score`
* `findings`
  * `severity`
  * `confidence`
  * `file_path`
  * `line_number`
  * `message`
  * `recommendation`
* `general_observations`

## Component discovery schema

For monorepo/component discovery, define a manifest schema:

* `component_name`
* `path`
* `languages`
* `frameworks`
* `included_paths`
* `excluded_paths`
* `capabilities`

## Validation and consistency

* Define schema validation rules for prompt and page metadata.
* Use a shared schema library or linting step for prompt files.
* Standardize taxonomy values for Pillars, Capabilities, Topics, languages, and tools.

## Open questions

* Which schema language should we use for validation: JSON Schema, YAML schema, or custom validators?
* Do we need separate schema versions for prompt pages and prompt exports?
* Should the root manifest support extensible metadata fields for future use?
