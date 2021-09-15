#!/bin/bash

#=================================================
# COMMON VARIABLES
#=================================================

# dependencies used by the app
pkg_dependencies=""

#=================================================
# PERSONAL HELPERS
#=================================================

# because ssbroom requires wildcard subdomains for aliases
# we need this custom function for creating the ssbroom nginx config
# instead of the standard ynh_add_nginx_config
add_ssb_room_nginx_config() {
    domain=$1
    domainregex=$(echo "$domain" | sed -r 's/\./\\\./g')
    # the sed statement above replaces all . with \.
    ynh_add_config --template="full_nginx.conf" --destination="/etc/nginx/conf.d/$domain.conf"
}

remove_ssb_room_nginx_config() {
    rm "/etc/nginx/conf.d/$domain.conf"
}

#=================================================
# EXPERIMENTAL HELPERS
#=================================================

#=================================================
# FUTURE OFFICIAL HELPERS
#=================================================


ynh_detect_arch(){
        local architecture
        if [ -n "$(uname -m | grep arm64)" ] || [ -n "$(uname -m | grep aarch64)" ]; then
                architecture="arm64"
        elif [ -n "$(uname -m | grep 64)" ]; then
                architecture="amd64"
        elif [ -n "$(uname -m | grep 86)" ]; then
                architecture="386"
        elif [ -n "$(uname -m | grep armv7)" ]; then
                architecture="arm7"
        elif [ -n "$(uname -m | grep armv6)" ]; then
                architecture="arm6"
        else
                architecture="unknown"
        fi
        echo $architecture
}