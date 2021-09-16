<!--
N.B.: This README was automatically generated by https://github.com/YunoHost/apps/tree/master/tools/README-generator
It shall NOT be edited by hand.
-->

# Scuttlebutt Room for YunoHost

[![Integration level](https://dash.yunohost.org/integration/ssbroom.svg)](https://dash.yunohost.org/appci/app/ssbroom) ![](https://ci-apps.yunohost.org/ci/badges/ssbroom.status.svg) ![](https://ci-apps.yunohost.org/ci/badges/ssbroom.maintain.svg)  
[![Install Scuttlebutt Room with YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=ssbroom)

*[Lire ce readme en français.](./README_fr.md)*

> *This package allows you to install Scuttlebutt Room quickly and simply on a YunoHost server.
If you don't have YunoHost, please consult [the guide](https://yunohost.org/#/install) to learn how to install it.*

## Overview

This is an SSB room server built in Go, packaged for yunohost. A room server is used to make connecting with friends easier on SSB apps. 
Room servers also makes it easy for any member to invite new folks, allowing the network to expand on its own. 

A more extensive document explaining how ssb room servers technically work can be found here: https://ssb-ngi-pointer.github.io/rooms2/

### Features

- SSB users can connect to the room and then create tunneled connections between each other.
- Admins of the SSB room can create invitations to invite new members.
- It is also possible, through settings, to allow new members to also invite new members (community mode).


**Shipped version:** 2.0.6~ynh1

**Demo:** https://hermies.club/

## Screenshots

![](./doc/screenshots/ssbroom-screenshot.png)

## Disclaimers / important information

* Current limitations:
    * requires a dedicated domain and can only run on the / path.
    * requires HTTPS
    * currently only supports amd64 architecture (hopefully getting more binaries from upstream soon)
    * uses own authentication mechanism (not SSO LDAP)
    * currently only supports one installation per server, and requires port 8008 specifically,
        but hopefully getting flexibility for other ports from upstream soon

## Documentation and resources

* Official app website: https://github.com/ssb-ngi-pointer/go-ssb-room
* Official user documentation: https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md
* Official admin documentation: https://github.com/ssb-ngi-pointer/go-ssb-room/blob/master/README.md
* Upstream app code repository: https://github.com/ssb-ngi-pointer/go-ssb-room
* YunoHost documentation for this app: https://yunohost.org/app_ssbroom
* Report a bug: https://github.com/YunoHost-Apps/ssbroom_ynh/issues

## Developer info

Please send your pull request to the [testing branch](https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing).

To try the testing branch, please proceed like that.
```
sudo yunohost app install https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
or
sudo yunohost app upgrade ssbroom -u https://github.com/YunoHost-Apps/ssbroom_ynh/tree/testing --debug
```

**More info regarding app packaging:** https://yunohost.org/packaging_apps