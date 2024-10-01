<!--
NB: Deze README is automatisch gegenereerd door <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Hij mag NIET handmatig aangepast worden.
-->

# Scuttlebutt Room voor Yunohost

[![Integratieniveau](https://dash.yunohost.org/integration/ssbroom.svg)](https://ci-apps.yunohost.org/ci/apps/ssbroom/) ![Mate van functioneren](https://ci-apps.yunohost.org/ci/badges/ssbroom.status.svg) ![Onderhoudsstatus](https://ci-apps.yunohost.org/ci/badges/ssbroom.maintain.svg)

[![Scuttlebutt Room met Yunohost installeren](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=ssbroom)

*[Deze README in een andere taal lezen.](./ALL_README.md)*

> *Met dit pakket kun je Scuttlebutt Room snel en eenvoudig op een YunoHost-server installeren.*  
> *Als je nog geen YunoHost hebt, lees dan [de installatiehandleiding](https://yunohost.org/install), om te zien hoe je 'm installeert.*

## Overzicht

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

**Geleverde versie:** 2.0.6~ynh8

**Demo:** <https://hermies.club/>

## Schermafdrukken

![Schermafdrukken van Scuttlebutt Room](./doc/screenshots/screenshot.png)

## Documentatie en bronnen

- Officiele gebruikersdocumentatie: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Officiele beheerdersdocumentatie: <https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md>
- Upstream app codedepot: <https://github.com/ssb-ngi-pointer/go-ssb-room>
- YunoHost-store: <https://apps.yunohost.org/app/ssbroom>
- Meld een bug: <https://github.com/YunoHost-Apps/ssbroom_ynh/issues>

## Ontwikkelaarsinformatie

Stuur je pull request alsjeblieft naar de [`testing`-branch](https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing).

Om de `testing`-branch uit te proberen, ga als volgt te werk:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
of
sudo yunohost app upgrade ssbroom -u https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
```

**Verdere informatie over app-packaging:** <https://yunohost.org/packaging_apps>
