package com.example.plugin.velocity

import com.google.inject.Inject
import com.velocitypowered.api.event.Subscribe
import com.velocitypowered.api.event.proxy.ProxyInitializeEvent
import com.velocitypowered.api.plugin.Plugin
import com.example.plugin.BuildConstants
import org.slf4j.Logger

@Plugin(
    id = "pluginname", name = "PluginName", version = BuildConstants.VERSION
)
class PluginName @Inject constructor(val logger: Logger) {

    @Subscribe
    fun onProxyInitialization(event: ProxyInitializeEvent) {
    }
}