# Repo Sense Website Requirements

This document defines the website-level requirements for Repo Sense.
It focuses on the user-facing product, navigation structure, content presentation, and hosting model.

## Purpose

* Define a consistent UI and content structure for Pillars, Capabilities, Topics, and Prompt assets.
* Capture website behavior, page templates, search capabilities, and deployment assumptions.

## Product scope

* Abilities: the composite assessment units that include Pillars, Capabilities, and Topics.
* Pillars: high-level assessment domains.
* Capabilities: grouped assessment areas within a Pillar.
* Topic: individual sub-items within a Capability.
* Prompt pages: metadata-backed prompt definitions that users can choose and export.
* Collectives: pre-built groupings of Pillars/Capabilities for common use cases like Production Readiness or Architecture Review.

## Page and content structure

### Pillar landing page

Each Pillar page should include:
* name and short summary
* purpose and why it matters
* related Capabilities
* example use cases
* tags and categories
* recommended automation tools and references
* links to related Pillars and collectives

### Capability page

Each Capability page should include:
* name and description
* objective and what it checks
* list of Topics under the Capability
* prompt recommendations, if applicable
* adoption guidance and best practices
* automation tools and implementation references
* common repo signs and relevant files

### Topic page

Each Topic page should include:
* name and summary
* what it looks for in a repository
* relevant prompts and collections
* example automation tools and references
* sample findings
* related Topics and Capabilities

### Prompt detail page

Each prompt page should include standard metadata:
* name
* description
* applicable Pillar / Capability / Topic
* use cases
* automation guidance
* impact
* best practices
* applicable languages/frameworks
* confidence/evidence requirements
* tags

## Search and discovery

* Provide search across Pillars, Capabilities, Topics, and Prompts.
* Support filtering by tags, use cases, applicable languages, and automation tools.
* Provide a landing page search bar and sidebar navigation for Pillars/Capabilities.

## Navigation

* Root homepage with quick access to Pillars, collectives, and featured workflows.
* Breadcrumbs for Pillar → Capability → Topic navigation.
* Search-driven discovery for prompt assets.
* Collection pages for pre-defined assessment bundles.

## Hosting and deployment

* Target static-first hosting for the initial version.
* Prefer GitHub Pages for the initial launch.
* Keep the content model compatible with file-based publishing.
* Design for future extension to dynamic backend if needed.
* Store prompt content and metadata directly in Git so the site can be generated from repository files.

## Legal and compliance

* Include a Terms & Conditions page.
* Include an advisory/disclaimer page that explains Repo Sense is advisory and not a substitute for professional review.
* Document any data handling expectations if user data is collected in the future.

## Open questions

* Should homepage show a catalog view or a workflow-driven onboarding experience?
* How should prompt downloads be packaged and presented to the user?
* What search UX should be used for large prompt catalogs?
* Do we need a content management path or only repo-based authoring?
