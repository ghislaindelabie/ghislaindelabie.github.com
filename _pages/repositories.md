---
layout: page
permalink: /repositories/
title: code
description: "Some pieces of work"
nav: true
nav_order: 4
lang: en
---

{% if site.data.repositories.github_users %}

## GitHub users
I’m fresh on the coding scene—you can see it in my stats. By comparison, my colleague Alex Bourreau, tech lead at [FabMob](https://lafabriquedesmobilites.fr/%C3%A0-propos/nous), has a far more seasoned footprint.
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for user in site.data.repositories.github_users %}
    {% include repository/repo_user.liquid username=user %}
  {% endfor %}
</div>

{% endif %}

{% if site.data.repositories.github_repos %}

## GitHub Repositories
Most repos here reflect my past role as product owner / facilitator—I guided the vision, rallied teams, and shipped through others’ keyboards. Going forward, you’ll see a shift: new projects will carry my own commits and pull-request scars. Scroll for the legacy work, stay tuned for the hands-on builds.
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.liquid repository=repo %}
  {% endfor %}
</div>
{% endif %}
