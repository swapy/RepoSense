# Repo Sense Abilities Structure

This folder contains the structured data and metadata for Repo Sense assessment abilities.
It separates page-level ability definitions from prompt metadata, schemas, and validation assets.

## Folder layout

* `abilities/pages/` - ability page definitions for Pillars, Capabilities, Topics, and Collectives.
* `abilities/prompts/` - prompt files and prompt metadata organized by the same ability taxonomy.
* `abilities/schemas/` - JSON/YAML schema definitions for ability pages, prompt metadata, root manifest, and report artifacts.
* `abilities/validation/` - validation rules, test fixtures, eval definitions, and guardrails.

## Schema separation

The repository maintains two distinct schema families:

* Ability/page schema: defines the descriptive data for Pillars, Capabilities, and Topics.
* Prompt metadata schema: defines the fields held by prompt definitions themselves.

## Next steps

1. Add ability page definitions under `abilities/pages/`.
2. Add prompt metadata and content under `abilities/prompts/`.
3. Add schema files under `abilities/schemas/`.
4. Add validation assets and prompt guardrails under `abilities/validation/`.
