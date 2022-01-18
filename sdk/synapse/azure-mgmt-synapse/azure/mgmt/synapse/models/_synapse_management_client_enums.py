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


class AzureADOnlyAuthenticationName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "default"

class AzureScaleType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Scale type.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    NONE = "none"

class BlobAuditingPolicyName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "default"

class BlobAuditingPolicyState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the state of the policy. If state is Enabled, storageEndpoint or
    isAzureMonitorTargetEnabled are required.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class BlobStorageEventType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The name of blob storage event type to process.
    """

    MICROSOFT_STORAGE_BLOB_CREATED = "Microsoft.Storage.BlobCreated"
    MICROSOFT_STORAGE_BLOB_RENAMED = "Microsoft.Storage.BlobRenamed"

class ClusterPrincipalRole(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Cluster principal role.
    """

    ALL_DATABASES_ADMIN = "AllDatabasesAdmin"
    ALL_DATABASES_VIEWER = "AllDatabasesViewer"

class ColumnDataType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The column data type.
    """

    IMAGE = "image"
    TEXT = "text"
    UNIQUEIDENTIFIER = "uniqueidentifier"
    DATE = "date"
    TIME = "time"
    DATETIME2 = "datetime2"
    DATETIMEOFFSET = "datetimeoffset"
    TINYINT = "tinyint"
    SMALLINT = "smallint"
    INT = "int"
    SMALLDATETIME = "smalldatetime"
    REAL = "real"
    MONEY = "money"
    DATETIME = "datetime"
    FLOAT = "float"
    SQL_VARIANT = "sql_variant"
    NTEXT = "ntext"
    BIT = "bit"
    DECIMAL = "decimal"
    NUMERIC = "numeric"
    SMALLMONEY = "smallmoney"
    BIGINT = "bigint"
    HIERARCHYID = "hierarchyid"
    GEOMETRY = "geometry"
    GEOGRAPHY = "geography"
    VARBINARY = "varbinary"
    VARCHAR = "varchar"
    BINARY = "binary"
    CHAR = "char"
    TIMESTAMP = "timestamp"
    NVARCHAR = "nvarchar"
    NCHAR = "nchar"
    XML = "xml"
    SYSNAME = "sysname"

class Compression(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The compression type
    """

    NONE = "None"
    G_ZIP = "GZip"

class ConfigurationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the spark config properties file.
    """

    FILE = "File"
    ARTIFACT = "Artifact"

class ConnectionPolicyName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "default"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class CreateMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the mode of sql pool creation.
    
    Default: regular sql pool creation.
    
    PointInTimeRestore: Creates a sql pool by restoring a point in time backup of an existing sql
    pool. sourceDatabaseId must be specified as the resource ID of the existing sql pool, and
    restorePointInTime must be specified.
    
    Recovery: Creates a sql pool by a geo-replicated backup. sourceDatabaseId  must be specified as
    the recoverableDatabaseId to restore.
    
    Restore: Creates a sql pool by restoring a backup of a deleted sql  pool. SourceDatabaseId
    should be the sql pool's original resource ID. SourceDatabaseId and sourceDatabaseDeletionDate
    must be specified.
    """

    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    RECOVERY = "Recovery"
    RESTORE = "Restore"

class DatabasePrincipalRole(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Database principal role.
    """

    ADMIN = "Admin"
    INGESTOR = "Ingestor"
    MONITOR = "Monitor"
    USER = "User"
    UNRESTRICTED_VIEWER = "UnrestrictedViewer"
    VIEWER = "Viewer"

class DataConnectionKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Kind of the endpoint for the data connection
    """

    EVENT_HUB = "EventHub"
    EVENT_GRID = "EventGrid"
    IOT_HUB = "IotHub"

class DataFlowComputeType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Compute type of the cluster which will execute data flow job.
    """

    GENERAL = "General"
    MEMORY_OPTIMIZED = "MemoryOptimized"
    COMPUTE_OPTIMIZED = "ComputeOptimized"

class DataMaskingFunction(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The masking function that is used for the data masking rule.
    """

    DEFAULT = "Default"
    CCN = "CCN"
    EMAIL = "Email"
    NUMBER = "Number"
    SSN = "SSN"
    TEXT = "Text"

class DataMaskingRuleState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The rule state. Used to delete a rule. To delete an existing rule, specify the schemaName,
    tableName, columnName, maskingFunction, and specify ruleState as disabled. However, if the rule
    doesn't already exist, the rule will be created with ruleState set to enabled, regardless of
    the provided value of ruleState.
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"

class DataMaskingState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the data masking policy.
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"

class DataWarehouseUserActivityName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    CURRENT = "current"

class DayOfWeek(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Day of maintenance window.
    """

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"

class DefaultPrincipalsModificationKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The default principals modification kind
    """

    UNION = "Union"
    REPLACE = "Replace"
    NONE = "None"

class EncryptionProtectorName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    CURRENT = "current"

class EventGridDataFormat(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The data format of the message. Optionally the data format can be added to each message.
    """

    MULTIJSON = "MULTIJSON"
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    SCSV = "SCSV"
    SOHSV = "SOHSV"
    PSV = "PSV"
    TXT = "TXT"
    RAW = "RAW"
    SINGLEJSON = "SINGLEJSON"
    AVRO = "AVRO"
    TSVE = "TSVE"
    PARQUET = "PARQUET"
    ORC = "ORC"
    APACHEAVRO = "APACHEAVRO"
    W3_CLOGFILE = "W3CLOGFILE"

class EventHubDataFormat(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The data format of the message. Optionally the data format can be added to each message.
    """

    MULTIJSON = "MULTIJSON"
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    SCSV = "SCSV"
    SOHSV = "SOHSV"
    PSV = "PSV"
    TXT = "TXT"
    RAW = "RAW"
    SINGLEJSON = "SINGLEJSON"
    AVRO = "AVRO"
    TSVE = "TSVE"
    PARQUET = "PARQUET"
    ORC = "ORC"
    APACHEAVRO = "APACHEAVRO"
    W3_CLOGFILE = "W3CLOGFILE"

class GeoBackupPolicyName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "Default"

class GeoBackupPolicyState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the geo backup policy.
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"

class IntegrationRuntimeAuthKeyName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The name of the authentication key to regenerate.
    """

    AUTH_KEY1 = "authKey1"
    AUTH_KEY2 = "authKey2"

class IntegrationRuntimeAutoUpdate(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The state of integration runtime auto update.
    """

    ON = "On"
    OFF = "Off"

class IntegrationRuntimeEdition(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The edition for the SSIS Integration Runtime
    """

    STANDARD = "Standard"
    ENTERPRISE = "Enterprise"

class IntegrationRuntimeEntityReferenceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of this referenced entity.
    """

    INTEGRATION_RUNTIME_REFERENCE = "IntegrationRuntimeReference"
    LINKED_SERVICE_REFERENCE = "LinkedServiceReference"

class IntegrationRuntimeInternalChannelEncryptionMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """It is used to set the encryption mode for node-node communication channel (when more than 2
    self-hosted integration runtime nodes exist).
    """

    NOT_SET = "NotSet"
    SSL_ENCRYPTED = "SslEncrypted"
    NOT_ENCRYPTED = "NotEncrypted"

class IntegrationRuntimeLicenseType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """License type for bringing your own license scenario.
    """

    BASE_PRICE = "BasePrice"
    LICENSE_INCLUDED = "LicenseIncluded"

class IntegrationRuntimeSsisCatalogPricingTier(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The pricing tier for the catalog database. The valid values could be found in
    https://azure.microsoft.com/en-us/pricing/details/sql-database/
    """

    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PREMIUM_RS = "PremiumRS"

class IntegrationRuntimeState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The state of integration runtime.
    """

    INITIAL = "Initial"
    STOPPED = "Stopped"
    STARTED = "Started"
    STARTING = "Starting"
    STOPPING = "Stopping"
    NEED_REGISTRATION = "NeedRegistration"
    ONLINE = "Online"
    LIMITED = "Limited"
    OFFLINE = "Offline"
    ACCESS_DENIED = "AccessDenied"

class IntegrationRuntimeType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of integration runtime.
    """

    MANAGED = "Managed"
    SELF_HOSTED = "SelfHosted"

class IntegrationRuntimeUpdateResult(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The result of the last integration runtime node update.
    """

    NONE = "None"
    SUCCEED = "Succeed"
    FAIL = "Fail"

class IotHubDataFormat(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The data format of the message. Optionally the data format can be added to each message.
    """

    MULTIJSON = "MULTIJSON"
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    SCSV = "SCSV"
    SOHSV = "SOHSV"
    PSV = "PSV"
    TXT = "TXT"
    RAW = "RAW"
    SINGLEJSON = "SINGLEJSON"
    AVRO = "AVRO"
    TSVE = "TSVE"
    PARQUET = "PARQUET"
    ORC = "ORC"
    APACHEAVRO = "APACHEAVRO"
    W3_CLOGFILE = "W3CLOGFILE"

class Kind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Kind of the database
    """

    READ_WRITE = "ReadWrite"
    READ_ONLY_FOLLOWING = "ReadOnlyFollowing"

class LanguageExtensionName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Language extension that can run within KQL query.
    """

    PYTHON = "PYTHON"
    R = "R"

class ManagedIdentitySqlControlSettingsModelPropertiesGrantSqlControlToManagedIdentityActualState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Actual state
    """

    ENABLING = "Enabling"
    ENABLED = "Enabled"
    DISABLING = "Disabling"
    DISABLED = "Disabled"
    UNKNOWN = "Unknown"

class ManagedIdentitySqlControlSettingsModelPropertiesGrantSqlControlToManagedIdentityDesiredState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Desired state
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ManagedIntegrationRuntimeNodeStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The managed integration runtime node status.
    """

    STARTING = "Starting"
    AVAILABLE = "Available"
    RECYCLING = "Recycling"
    UNAVAILABLE = "Unavailable"

class ManagementOperationState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The operation state.
    """

    PENDING = "Pending"
    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCEL_IN_PROGRESS = "CancelInProgress"
    CANCELLED = "Cancelled"

class NodeSize(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The level of compute power that each node in the Big Data pool has.
    """

    NONE = "None"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    X_LARGE = "XLarge"
    XX_LARGE = "XXLarge"
    XXX_LARGE = "XXXLarge"

class NodeSizeFamily(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of nodes that the Big Data pool provides.
    """

    NONE = "None"
    MEMORY_OPTIMIZED = "MemoryOptimized"
    HARDWARE_ACCELERATED_FPGA = "HardwareAcceleratedFPGA"
    HARDWARE_ACCELERATED_GPU = "HardwareAcceleratedGPU"

class OperationStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Operation status
    """

    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"

class PrincipalsModificationKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The principals modification kind of the database
    """

    UNION = "Union"
    REPLACE = "Replace"
    NONE = "None"

class PrincipalType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Principal type.
    """

    APP = "App"
    GROUP = "Group"
    USER = "User"

class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Resource provisioning state
    """

    PROVISIONING = "Provisioning"
    SUCCEEDED = "Succeeded"
    DELETING = "Deleting"
    FAILED = "Failed"
    DELETE_ERROR = "DeleteError"

class QueryAggregationFunction(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The function that is used to aggregate each query's metrics.
    """

    MIN = "min"
    MAX = "max"
    AVG = "avg"
    SUM = "sum"

class QueryExecutionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The execution type that is used to filter the query instances that are returned.
    """

    ANY = "any"
    REGULAR = "regular"
    IRREGULAR = "irregular"
    ABORTED = "aborted"
    EXCEPTION = "exception"

class QueryMetricUnit(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The unit of measurement
    """

    PERCENTAGE = "percentage"
    KB = "KB"
    MICROSECONDS = "microseconds"

class QueryObservedMetricType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of metric to use for ordering the top metrics.
    """

    CPU = "cpu"
    IO = "io"
    LOGIO = "logio"
    DURATION = "duration"
    EXECUTION_COUNT = "executionCount"

class Reason(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Message providing the reason why the given name is invalid.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"

class RecommendedSensitivityLabelUpdateKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    ENABLE = "enable"
    DISABLE = "disable"

class ReplicationRole(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The role of the Sql pool in the replication link.
    """

    PRIMARY = "Primary"
    SECONDARY = "Secondary"
    NON_READABLE_SECONDARY = "NonReadableSecondary"
    SOURCE = "Source"
    COPY = "Copy"

class ReplicationState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The replication state for the replication link.
    """

    PENDING = "PENDING"
    SEEDING = "SEEDING"
    CATCH_UP = "CATCH_UP"
    SUSPENDED = "SUSPENDED"

class ResourceIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of managed identity for the workspace
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"

class ResourceProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioned state of the resource.
    """

    RUNNING = "Running"
    CREATING = "Creating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    MOVING = "Moving"
    CANCELED = "Canceled"

class RestorePointType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of restore point
    """

    CONTINUOUS = "CONTINUOUS"
    DISCRETE = "DISCRETE"

class SecurityAlertPolicyName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "default"

class SecurityAlertPolicyNameAutoGenerated(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "Default"

class SecurityAlertPolicyState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the state of the policy, whether it is enabled or disabled or a policy has not been
    applied yet on the specific Sql pool.
    """

    NEW = "New"
    ENABLED = "Enabled"
    DISABLED = "Disabled"

class SelfHostedIntegrationRuntimeNodeStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the integration runtime node.
    """

    NEED_REGISTRATION = "NeedRegistration"
    ONLINE = "Online"
    LIMITED = "Limited"
    OFFLINE = "Offline"
    UPGRADING = "Upgrading"
    INITIALIZING = "Initializing"
    INITIALIZE_FAILED = "InitializeFailed"

class SensitivityLabelRank(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "None"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class SensitivityLabelSource(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    CURRENT = "current"
    RECOMMENDED = "recommended"

class SensitivityLabelUpdateKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    SET = "set"
    REMOVE = "remove"

class ServerKeyType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The encryption protector type like 'ServiceManaged', 'AzureKeyVault'.
    """

    SERVICE_MANAGED = "ServiceManaged"
    AZURE_KEY_VAULT = "AzureKeyVault"

class SkuName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """SKU name.
    """

    COMPUTE_OPTIMIZED = "Compute optimized"
    STORAGE_OPTIMIZED = "Storage optimized"

class SkuSize(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """SKU size.
    """

    EXTRA_SMALL = "Extra small"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

class SsisObjectMetadataType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of SSIS object metadata.
    """

    FOLDER = "Folder"
    PROJECT = "Project"
    PACKAGE = "Package"
    ENVIRONMENT = "Environment"

class State(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the resource.
    """

    CREATING = "Creating"
    UNAVAILABLE = "Unavailable"
    RUNNING = "Running"
    DELETING = "Deleting"
    DELETED = "Deleted"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    STARTING = "Starting"
    UPDATING = "Updating"

class StateValue(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """property configuration state
    """

    CONSISTENT = "Consistent"
    IN_CONSISTENT = "InConsistent"
    UPDATING = "Updating"

class StorageAccountType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The storage account type used to store backups for this sql pool.
    """

    GRS = "GRS"
    LRS = "LRS"

class TransparentDataEncryptionName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    CURRENT = "current"

class TransparentDataEncryptionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the database transparent data encryption.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class Type(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of resource, for instance Microsoft.Synapse/workspaces/kustoPools/databases.
    """

    MICROSOFT_SYNAPSE_WORKSPACES_KUSTO_POOLS_DATABASES = "Microsoft.Synapse/workspaces/kustoPools/databases"
    MICROSOFT_SYNAPSE_WORKSPACES_KUSTO_POOLS_ATTACHED_DATABASE_CONFIGURATIONS = "Microsoft.Synapse/workspaces/kustoPools/attachedDatabaseConfigurations"

class VulnerabilityAssessmentName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "default"

class VulnerabilityAssessmentPolicyBaselineName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    MASTER = "master"
    DEFAULT = "default"

class VulnerabilityAssessmentScanState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The scan status.
    """

    PASSED = "Passed"
    FAILED = "Failed"
    FAILED_TO_RUN = "FailedToRun"
    IN_PROGRESS = "InProgress"

class VulnerabilityAssessmentScanTriggerType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The scan trigger type.
    """

    ON_DEMAND = "OnDemand"
    RECURRING = "Recurring"

class WorkspacePublicNetworkAccess(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enable or Disable public network access to workspace
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"
