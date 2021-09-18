# Scuttlebutt Room pour YunoHost

[![Niveau d'intégration](https://dash.yunohost.org/integration/ssbroom.svg)](https://dash.yunohost.org/appci/app/ssbroom) ![](https://ci-apps.yunohost.org/ci/badges/ssbroom.status.svg) ![](https://ci-apps.yunohost.org/ci/badges/ssbroom.maintain.svg)  
[![Installer Scuttlebutt Room avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=ssbroom)

*[Read this readme in english.](./README.md)*
*[Lire ce readme en français.](./README_fr.md)*

> *Ce package vous permet d'installer Scuttlebutt Room rapidement et simplement sur un serveur YunoHost.
Si vous n'avez pas YunoHost, regardez [ici](https://yunohost.org/#/install) pour savoir comment l'installer et en profiter.*

## Vue d'ensemble

Some long and extensive description of what the app is and does, lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

### Features

- Ut enim ad minim veniam, quis nostrud exercitation ullamco ;
- Laboris nisi ut aliquip ex ea commodo consequat ;
- Duis aute irure dolor in reprehenderit in voluptate ;
- Velit esse cillum dolore eu fugiat nulla pariatur ;
- Excepteur sint occaecat cupidatat non proident, sunt in culpa."


**Version incluse :** 2.0.6~ynh1

**Démo :** https://hermies.club/

## Captures d'écran

![](./doc/screenshots/ssbroom-screenshot.png)
![](./doc/screenshots/example.jpg)

## Avertissements / informations importantes

* Any known limitations, constrains or stuff not working, such as (but not limited to):
    * requiring a full dedicated domain ?
    * architectures not supported ?
    * not-working single-sign on or LDAP integration ?
    * the app requires an important amount of RAM / disk / .. to install or to work properly
    * etc...

* Other infos that people should be aware of, such as:
    * any specific step to perform after installing (such as manually finishing the install, specific admin credentials, ...)
    * how to configure / administrate the application if it ain't obvious
    * upgrade process / specificities / things to be aware of ?
    * security considerations ?

## Documentations et ressources

* Site officiel de l'app : https://github.com/ssb-ngi-pointer/go-ssb-room
* Documentation officielle utilisateur : https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md
* Documentation officielle de l'admin : https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md
* Dépôt de code officiel de l'app : https://github.com/ssb-ngi-pointer/go-ssb-room
* Documentation YunoHost pour cette app : https://yunohost.org/app_ssbroom
* Signaler un bug : https://github.com/YunoHost-Apps/ssbroom_ynh/issues

## Informations pour les développeurs

Merci de faire vos pull request sur la [branche testing](https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing).

Pour essayer la branche testing, procédez comme suit.
```
sudo yunohost app install https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
ou
sudo yunohost app upgrade ssbroom -u https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
```

**Plus d'infos sur le packaging d'applications :** https://yunohost.org/packaging_apps