# Repo Sense Prompt Requirements

This document defines the requirements for prompt-level content and standardization.
It focuses on the prompt schema, content model, metadata, and how prompts are represented.

## Purpose

* Define a canonical prompt metadata schema.
* Standardize prompt content and presentation.
* Ensure consistency across all prompt definitions and prompt pages.

## Core prompt concepts

* Ability: a generic assessment unit that can refer to a Pillar, Capability, or Topic.
* Ability page: the structured page-level model for a Pillar, Capability, or Topic ability.
* Prompt: the individual AI assessment instruction or check.
* Prompt page: the web page that describes the prompt and its usage.
* Prompt metadata: structured fields used to describe the prompt.
* Prompt bundle: a set of prompts exported together for a selected assessment.

## Schema separation

Repo Sense uses two separate schema families:

* Ability/page schema: defines the descriptive data for Pillars, Capabilities, and Topics, including description, impact, automation tools, references, and related prompts.
* Prompt metadata schema: defines the fields held by a prompt itself, including prompt body, automation guidance, evidence requirements, and metadata used for exports and validation.

These two schemas should remain distinct and should not be mixed.

## Required prompt metadata

Each prompt should include standard fields. If using file-based storage, these fields should be part of the prompt metadata or frontmatter.

### Minimum required fields

* `id` (stable prompt identifier)
* `name`
* `description`
* `pillar`
* `capability`
* `topic`
* `use_cases`
* `automation_guidance`
* `impact`
* `best_practices`
* `applicable_languages`
* `confidence`
* `evidence_requirements`
* `status` (`draft`, `review`, `published`)

### Recommended fields

* `tags`
* `downloads`
* `version`
* `change_notes`
* `author`
* `created_at`
* `updated_at`
* `related_prompts`
* `recommended_tools`
* `severity`
* `weight`
* `coverage`

### Nice-to-have fields

* `compliance_references`
* `validation_examples`
* `output_schema`
* `component_types`
* `assessment_strategy`
* `input_hints`
* `example_responses`
* `review_status`
* `reviewer`
* `estimated_effort`
* `confidence_rationale`

## Prompt content format

* Prefer Markdown with YAML frontmatter for prompts and metadata.
* Each prompt file should contain:
  * metadata header
  * prompt body
  * examples or guidance sections, if applicable
* Store prompt files in Git, organized by Pillar / Capability / Topic folder structure.
* Each item folder may also include:
  * `images/` for diagrams or visual assets
  * supporting files required by the prompt
* Alternative storage may use JSON or YAML objects when needed, but the primary model is file-based.

## Prompt standardization rules

* All prompt metadata should use consistent field names and value types.
* Use controlled vocabularies for taxonomy-driven fields and classification tags.
* Standardize tags, tool names, language identifiers, confidence values, and status values.
* Keep prompt bodies modular and reusable where possible.

## Controlled taxonomy

Repo Sense must enforce a controlled taxonomy model for prompt metadata.
The controlled taxonomy should apply to:

* `pillar`
* `capability`
* `topic`
* `applicable_languages`
* `recommended_tools`
* `tags`
* `confidence`
* `status`
* `severity`

Recommended controlled vocabularies:

* Pillars: Security, Observability, Documentation, DevOps, API Strategy, Developer Experience, Reliability, Maintainability, Performance, Scalability, Testing, Compliance, Version Control, Configuration, Errors, Language & Framework Best Practices
* Confidence: `high`, `medium`, `low`
* Status: `draft`, `review`, `published`, `deprecated`
* Severity: `critical`, `high`, `medium`, `low`

A practical implementation should use the same controlled values in both prompt frontmatter and generated prompt indexes.

## Prompt lifecycle requirements

* Define how prompts are added, reviewed, and updated.
* Decide whether prompts require a review step before publishing.
* Define how prompt deprecation is handled.
* Record change details without making versioning overly complex.

## Prompt ground rules

Every prompt must obey the platform’s assessment constraints. In particular:

* No edit policy: prompts may assess, recommend, or describe required changes, but they must never instruct the AI to directly modify, generate, or patch repository code.
* Privacy and data hygiene: prompts must avoid requesting or retaining PII, credentials, secrets, or other sensitive repository data.
* Evidence-first guidance: prompts should require clear evidence attribution such as file paths, line numbers, or exact configuration references.
* Scope discipline: each prompt should remain clearly scoped to a single Topic or assessment objective.
* Hallucination control: prompts must require uncertain findings to be labeled as “Potential” or “Needs verification” rather than asserted as fact.

## Prompt testing and validation

Prompt quality is a core requirement for Repo Sense. The platform must support prompt testing and evaluation before prompts are published or exported.

* Define a test framework or evals process for prompt validation.
* Validate that prompts use the controlled taxonomy and correct metadata fields.
* Ensure prompts do not break the no-code-edit ground rule.
* Include checks for prompt clarity, expected output structure, and confidence labeling.
* Keep test artifacts as first-class assets alongside prompt definitions.

## Prompt export requirements

* Prompt bundles should be exportable as ZIP packages.
* Each bundle should include:
  * root manifest file
  * selected prompt documents
  * optional metadata index
* The root manifest should define the execution order and onboarding instruction for the AI tool.

## Open questions

* Should prompt files be stored directly in the repository or generated from a metadata-first source?
* How much of the prompt body should be templated vs bespoke per prompt?
* What minimum prompt metadata should be enforced for MVP?
* Should prompt metadata include automation tool compatibility lists?
