---
layout: page
permalink: /repositories/
title: code
description: "Quelques projets auxquels j'ai contribué"
nav: true
nav_order: 4
lang: fr
---

{% if site.data.repositories.github_users %}

## Utilisateurs GitHub
Je débute encore dans le code — mes stats le montrent ! En comparaison, mon collègue Alex Bourreau, tech lead chez [FabMob](https://lafabriquedesmobilites.fr/%C3%A0-propos/nous), affiche un tout autre niveau d’expertise.
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for user in site.data.repositories.github_users %}
    {% include repository/repo_user.liquid username=user %}
  {% endfor %}
</div>

{% endif %}

{% if site.data.repositories.github_repos %}

## Dépôts GitHub
Beaucoup de ces dépôts illustrent mon rôle passé de Product Owner / facilitateur : j’y ai porté la vision, fédéré les équipes et livré via les claviers d’autres contributeurs. Désormais, cap sur du concret : les prochains projets porteront ma propre signature, commits et pull-requests à l’appui. Explorez les réalisations existantes et revenez vite pour découvrir mes futurs chantiers "mains-dans-le-code" !
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.liquid repository=repo %}
  {% endfor %}
</div>
{% endif %}
