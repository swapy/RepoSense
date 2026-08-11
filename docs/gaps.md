# Gaps and Open Points for Repo Sense

This document captures all implementation gaps, open questions, and standardization needs prior to building the product.

## High-level missing definitions

* Prompt/module metadata schema is not yet specified in a concrete format.
* Site structure and navigation flow are not fully defined (Pillars → Capabilities → Topic pages).
* Search and discovery design is not defined (client-side vs backend indexing vs external search).
* Scoring model and aggregation formula are not defined.
* Catalog source-of-truth is not decided: file-based repo content vs backend-managed data.
* Runtime vs static architecture is not decided for the initial version.
* Role/permission requirements are not defined, if a web app will require user management.

For deeper clarity, these requirements are now broken into dedicated documents:
* `website-requirements.md` — website-level product and UI requirements
* `prompt-requirements.md` — prompt-level content and metadata requirements
* `orchestration-requirements.md` — execution, orchestration, and reporting requirements
* `schema-requirements.md` — standardized schema definitions and validation

## Prompt page metadata gaps

* Define the exact schema for prompt metadata fields:
  * name
  * description
  * downloads / adoption
  * applicable languages / frameworks
  * use cases
  * automation guidance
  * impact
  * best practices
  * related checks
  * confidence / evidence
* Clarify whether these fields are stored in Markdown frontmatter, JSON files, or a database.
* Decide if metadata needs a standardized taxonomy for use cases, automation tools, and impact categories.

## Product naming and UI gaps

* Confirm whether the product name is `Repo Sense` across documentation and website assets.
* Standardize language: Pillars, Capabilities, Topic.
* Decide the exact wording for the web app's T&C and disclaimer pages.
* Define the page templates and content layout for each Pillar / Capability / Topic detail page.

## Orchestration and repository analysis gaps

* Define the contract for polyglot/monorepo orchestration and component sets.
* Document how shared files and cross-cutting concerns should be assigned to Pillars or Capabilities.
* Define the discovery manifest format for component sets, e.g. `reposense.component.yaml`.
* Define how prompt execution is scoped for per-language or per-service boundaries.

## Reporting and scoring gaps

* Define the scoring dimensions, scale, and how severity maps to numeric values.
* Define how Topic scores aggregate into Capability scores and Pillar scores.
* Specify how confidence and evidence should be represented in report output.
* Define the final weighted Global Repository Score calculation.

## Content and taxonomy gaps

* Clarify `AI Slop` coverage and the exact pass/fail criteria for this Pillar.
* Map overlapping Pillars such as Security/Configuration, Reliability/Errors, Performance/Scalability.
* Define role-based bundles for common audiences (security review, platform readiness, developer onboarding).
* Decide whether some Capabilities should be mandatory for specific repository types.

## Hosting and implementation gaps

* Confirm the initial hosting model: GitHub Pages / static site vs dynamic web app.
* Decide whether a database is needed for any first-phase features.
* If free hosting is required, determine which features must be postponed until later.
* Define the content update workflow for prompt metadata and site publishing.

## Legal and risk gaps

* Formalize the terms and conditions language for the website.
* Document the liability disclaimer and usage guidance clearly for users.
* Decide if the product needs additional legal copy for GDPR / privacy if user data is stored.

## General open points

* Decide how prompts and modules will be versioned or changed over time without creating an overly rigid model.
* Finalize the actual product page hierarchy and navigation model before implementation.
* Identify the minimum viable feature set for the first launch.
* Define the expected developer workflow for adding new Capabilities and Topic pages.



