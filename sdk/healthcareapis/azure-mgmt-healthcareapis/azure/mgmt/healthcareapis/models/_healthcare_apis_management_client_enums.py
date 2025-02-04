# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class ActionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs.
    """

    INTERNAL = "Internal"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class FhirResourceVersionPolicy(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Controls how resources are versioned on the FHIR service
    """

    NO_VERSION = "no-version"
    VERSIONED = "versioned"
    VERSIONED_UPDATE = "versioned-update"

class FhirServiceKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of the service.
    """

    FHIR_STU3 = "fhir-Stu3"
    FHIR_R4 = "fhir-R4"

class IotIdentityResolutionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of IoT identity resolution to use with the destination.
    """

    CREATE = "Create"
    LOOKUP = "Lookup"

class Kind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of the service.
    """

    FHIR = "fhir"
    FHIR_STU3 = "fhir-Stu3"
    FHIR_R4 = "fhir-R4"

class ManagedServiceIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of identity being specified, currently SystemAssigned and None are allowed.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"

class OperationResultStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the operation being performed.
    """

    CANCELED = "Canceled"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    REQUESTED = "Requested"
    RUNNING = "Running"

class PrivateEndpointConnectionProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The current provisioning state.
    """

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"

class PrivateEndpointServiceConnectionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The private endpoint connection status.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state.
    """

    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    ACCEPTED = "Accepted"
    VERIFYING = "Verifying"
    UPDATING = "Updating"
    FAILED = "Failed"
    CANCELED = "Canceled"
    DEPROVISIONED = "Deprovisioned"
    MOVING = "Moving"
    SUSPENDED = "Suspended"
    WARNED = "Warned"
    SYSTEM_MAINTENANCE = "SystemMaintenance"

class PublicNetworkAccess(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Control permission for data plane traffic coming from public networks while private endpoint is
    enabled.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ServiceEventState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the current status of event support for the resource.
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"
    UPDATING = "Updating"

class ServiceManagedIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of identity being specified, currently SystemAssigned and None are allowed.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"

class ServiceNameUnavailabilityReason(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The reason for unavailability.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"
