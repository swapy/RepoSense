# Repo Sense Orchestration Requirements

This document defines the execution and reporting requirements for Repo Sense.
It focuses on how prompts are selected, how analysis is scoped, and how outputs are generated.

## Purpose

* Define the assessment orchestration model.
* Describe the repository analysis workflow.
* Standardize result reporting and score aggregation.

## Orchestration model

* User selects Pillars, Capabilities, Topics, or Collectives.
* Selected prompts are packaged into an export bundle.
* The root manifest coordinates prompt execution and provides AI instructions.
* The root manifest schema is defined in `docs/schema-requirements.md` and should be treated as ready for export bundle validation.

## Repository analysis workflow

* Identify the repository entry point and relevant manifests.
* Detect languages, frameworks, and component boundaries.
* Partition analysis into component sets for polyglot or monorepo repos.
* Scope prompts to the appropriate files or folders.

## Prompt selection and grouping

* Prompt selection should respect user choices at each hierarchy level.
* Provide clear grouping rules when multiple Capabilities overlap.
* Allow users to refine selections before exporting.

## Polyglot and monorepo handling

* Define how mixed-language repositories are discovered and partitioned.
* Specify how shared configuration files are handled.
* Use a discovery manifest such as `reposense.component.yaml` for explicit component boundaries.
* Define fallback rules for repositories without explicit manifests.

## Reporting requirements

* Output reports should include:
  * findings and observations
  * severity levels
  * confidence and evidence references
  * scoring breakdown by Topic, Capability, and Pillar
  * global repository score
* Include a `General Observations` section for risks outside defined Pillars.

## Score aggregation

* Define the scoring scale (e.g. 0-100 or 1-5).
* Define how Topic scores aggregate into Capability scores.
* Define how Capability scores aggregate into Pillar scores.
* Define the global score calculation.
* Define how missing data or skipped prompts affect scores.

## Output formats

* Define the root manifest schema for exported bundles.
* Define report output formats for AI tools, e.g. JSON, Markdown, or HTML.
* Define the structure for evidence attribution, including file paths and lines.

## Open questions

* Should orchestration be handled entirely by the AI tool using the root manifest, or do we need a local execution engine?
* How should we manage prompt execution state and retries?
* What level of granularity is required for component set boundaries?
* How should the system handle partial or incomplete repository scans?
