<!--
Nota bene : ce README est automatiquement généré par <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Il NE doit PAS être modifié à la main.
-->

# Scuttlebutt Room pour YunoHost

[![Niveau d’intégration](https://dash.yunohost.org/integration/ssbroom.svg)](https://dash.yunohost.org/appci/app/ssbroom) ![Statut du fonctionnement](https://ci-apps.yunohost.org/ci/badges/ssbroom.status.svg) ![Statut de maintenance](https://ci-apps.yunohost.org/ci/badges/ssbroom.maintain.svg)

[![Installer Scuttlebutt Room avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=ssbroom)

*[Lire le README dans d'autres langues.](./ALL_README.md)*

> *Ce package vous permet d’installer Scuttlebutt Room rapidement et simplement sur un serveur YunoHost.*  
> *Si vous n’avez pas YunoHost, consultez [ce guide](https://yunohost.org/install) pour savoir comment l’installer et en profiter.*

## Vue d’ensemble

A Scuttlebutt room is a service for connecting scuttlebutt users.

It includes a web interface for managing who is in the room, creating invites, and creating a code of conduct for the room.

For a comprehensive introduction to rooms 2.0, watch [this video](https://www.youtube.com/watch?v=W5p0y_MWwDE).

### Features

- Rooms v1 (tunnel.connect, tunnel.endpoints, etc.)
- User management (allow- & denylisting + moderator & administrator roles), all administered via the web dashboard
- Multiple privacy modes
- Sign-in with SSB
- HTTP Invites
- Alias management

**Version incluse :** 2.0.6~ynh8

**Démo :** <https://hermies.club/>

## Captures d’écran

![Capture d’écran de Scuttlebutt Room](./doc/screenshots/screenshot.png)

## Documentations et ressources

- Documentation officielle utilisateur : <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Documentation officielle de l’admin : <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Dépôt de code officiel de l’app : <https://github.com/ssb-ngi-pointer/go-ssb-room>
- YunoHost Store : <https://apps.yunohost.org/app/ssbroom>
- Signaler un bug : <https://github.com/YunoHost-Apps/ssbroom_ynh/issues>

## Informations pour les développeurs

Merci de faire vos pull request sur la [branche `testing`](https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing).

Pour essayer la branche `testing`, procédez comme suit :

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
ou
sudo yunohost app upgrade ssbroom -u https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
```

**Plus d’infos sur le packaging d’applications :** <https://yunohost.org/packaging_apps>
