# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class ApplicationGatewayCookieBasedAffinity(str, Enum):
    """Cookie based affinity. Possible values are: 'Enabled' and 'Disabled'.
    """

    enabled = "Enabled"
    disabled = "Disabled"

class ApplicationGatewayOperationalState(str, Enum):
    """Operational state of the application gateway resource. Possible values are: 'Stopped',
    'Started', 'Running', and 'Stopping'.
    """

    stopped = "Stopped"
    starting = "Starting"
    running = "Running"
    stopping = "Stopping"

class ApplicationGatewayProtocol(str, Enum):
    """Protocol. Possible values are: 'Http' and 'Https'.
    """

    http = "Http"
    https = "Https"

class ApplicationGatewayRequestRoutingRuleType(str, Enum):
    """Rule type. Possible values are: 'Basic' and 'PathBasedRouting'.
    """

    basic = "Basic"
    path_based_routing = "PathBasedRouting"

class ApplicationGatewaySkuName(str, Enum):
    """Name of an application gateway SKU. Possible values are: 'Standard_Small', 'Standard_Medium',
    'Standard_Large', 'WAF_Medium', and 'WAF_Large'.
    """

    standard_small = "Standard_Small"
    standard_medium = "Standard_Medium"
    standard_large = "Standard_Large"

class AuthorizationUseStatus(str, Enum):
    """AuthorizationUseStatus. Possible values are: 'Available' and 'InUse'.
    """

    available = "Available"
    in_use = "InUse"

class ExpressRouteCircuitPeeringAdvertisedPublicPrefixState(str, Enum):
    """AdvertisedPublicPrefixState of the Peering resource. Possible values are 'NotConfigured',
    'Configuring', 'Configured', and 'ValidationNeeded'.
    """

    not_configured = "NotConfigured"
    configuring = "Configuring"
    configured = "Configured"
    validation_needed = "ValidationNeeded"

class ExpressRouteCircuitPeeringState(str, Enum):
    """The state of peering. Possible values are: 'Disabled' and 'Enabled'
    """

    disabled = "Disabled"
    enabled = "Enabled"

class ExpressRouteCircuitPeeringType(str, Enum):
    """The PeeringType. Possible values are: 'AzurePublicPeering', 'AzurePrivatePeering', and
    'MicrosoftPeering'.
    """

    azure_public_peering = "AzurePublicPeering"
    azure_private_peering = "AzurePrivatePeering"
    microsoft_peering = "MicrosoftPeering"

class ExpressRouteCircuitSkuFamily(str, Enum):
    """The family of the SKU. Possible values are: 'UnlimitedData' and 'MeteredData'.
    """

    unlimited_data = "UnlimitedData"
    metered_data = "MeteredData"

class ExpressRouteCircuitSkuTier(str, Enum):
    """The tier of the SKU. Possible values are 'Standard' and 'Premium'.
    """

    standard = "Standard"
    premium = "Premium"

class IPAllocationMethod(str, Enum):
    """PrivateIP allocation method. Possible values are: 'Static' and 'Dynamic'.
    """

    static = "Static"
    dynamic = "Dynamic"

class LoadDistribution(str, Enum):
    """The load distribution policy for this rule. Possible values are 'Default', 'SourceIP', and
    'SourceIPProtocol'.
    """

    default = "Default"
    source_ip = "SourceIP"
    source_ip_protocol = "SourceIPProtocol"

class NetworkOperationStatus(str, Enum):
    """Status of the Azure async operation. Possible values are: 'InProgress', 'Succeeded', and
    'Failed'.
    """

    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"

class ProbeProtocol(str, Enum):
    """The protocol of the end point. Possible values are: 'Http' or 'Tcp'. If 'Tcp' is specified, a
    received ACK is required for the probe to be successful. If 'Http' is specified, a 200 OK
    response from the specifies URI is required for the probe to be successful.
    """

    http = "Http"
    tcp = "Tcp"

class ProcessorArchitecture(str, Enum):
    """VPN client Processor Architecture. Possible values are: 'AMD64' and 'X86'.
    """

    amd64 = "Amd64"
    x86 = "X86"

class RouteNextHopType(str, Enum):
    """Gets NextHopType.
    """

    virtual_network_gateway = "VirtualNetworkGateway"
    vnet_local = "VnetLocal"
    internet = "Internet"
    virtual_appliance = "VirtualAppliance"
    none = "None"

class SecurityRuleAccess(str, Enum):
    """The network traffic is allowed or denied. Possible values are: 'Allow' and 'Deny'.
    """

    allow = "Allow"
    deny = "Deny"

class SecurityRuleDirection(str, Enum):
    """The direction of the rule. The direction specifies if rule will be evaluated on incoming or
    outgoing traffic. Possible values are: 'Inbound' and 'Outbound'.
    """

    inbound = "Inbound"
    outbound = "Outbound"

class SecurityRuleProtocol(str, Enum):
    """Network protocol this rule applies to. Possible values are 'Tcp', 'Udp', and '*'.
    """

    tcp = "Tcp"
    udp = "Udp"
    asterisk = "*"

class ServiceProviderProvisioningState(str, Enum):
    """The ServiceProviderProvisioningState state of the resource. Possible values are
    'NotProvisioned', 'Provisioning', 'Provisioned', and 'Deprovisioning'.
    """

    not_provisioned = "NotProvisioned"
    provisioning = "Provisioning"
    provisioned = "Provisioned"
    deprovisioning = "Deprovisioning"

class TransportProtocol(str, Enum):
    """The transport protocol for the external endpoint. Possible values are 'Udp' or 'Tcp'
    """

    udp = "Udp"
    tcp = "Tcp"

class VirtualNetworkGatewayConnectionStatus(str, Enum):
    """Virtual network Gateway connection status. Possible values are 'Unknown', 'Connecting',
    'Connected' and 'NotConnected'.
    """

    unknown = "Unknown"
    connecting = "Connecting"
    connected = "Connected"
    not_connected = "NotConnected"

class VirtualNetworkGatewayConnectionType(str, Enum):
    """Gateway connection type. Possible values are: 'IPsec','Vnet2Vnet','ExpressRoute', and
    'VPNClient.
    """

    i_psec = "IPsec"
    vnet2_vnet = "Vnet2Vnet"
    express_route = "ExpressRoute"
    vpn_client = "VPNClient"

class VirtualNetworkGatewaySkuName(str, Enum):
    """Gateway sku name -Basic/HighPerformance/Standard
    """

    basic = "Basic"
    high_performance = "HighPerformance"
    standard = "Standard"

class VirtualNetworkGatewaySkuTier(str, Enum):
    """Gateway sku tier -Basic/HighPerformance/Standard
    """

    basic = "Basic"
    high_performance = "HighPerformance"
    standard = "Standard"

class VirtualNetworkGatewayType(str, Enum):
    """The type of this virtual network gateway. Possible values are: 'Vpn' and 'ExpressRoute'.
    """

    vpn = "Vpn"
    express_route = "ExpressRoute"

class VpnType(str, Enum):
    """The type of this virtual network gateway. Possible values are: 'PolicyBased' and 'RouteBased'.
    """

    policy_based = "PolicyBased"
    route_based = "RouteBased"
