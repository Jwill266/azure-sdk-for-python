# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class CleanupOptions(str, Enum):
    """The clean up preference when the script execution gets in a terminal state. Default setting is
    'Always'.
    """

    always = "Always"
    on_success = "OnSuccess"
    on_expiration = "OnExpiration"

class CreatedByType(str, Enum):
    """The type of identity that created the resource.
    """

    user = "User"
    application = "Application"
    managed_identity = "ManagedIdentity"
    key = "Key"

class ScriptProvisioningState(str, Enum):
    """State of the script execution. This only appears in the response.
    """

    creating = "Creating"
    provisioning_resources = "ProvisioningResources"
    running = "Running"
    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"

class ScriptType(str, Enum):
    """Type of the script.
    """

    azure_power_shell = "AzurePowerShell"
    azure_cli = "AzureCLI"
