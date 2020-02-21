# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6198, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class DiscoveryStatus(str, Enum):

    unknown = "Unknown"
    not_started = "NotStarted"
    in_progress = "InProgress"
    completed = "Completed"

class ProvisioningState(str, Enum):

    accepted = "Accepted"
    creating = "Creating"
    deleting = "Deleting"
    failed = "Failed"
    moving = "Moving"
    succeeded = "Succeeded"

class MachineBootType(str, Enum):

    unknown = "Unknown"
    efi = "EFI"
    bios = "BIOS"

class AzureLocation(str, Enum):

    unknown = "Unknown"
    east_asia = "EastAsia"
    southeast_asia = "SoutheastAsia"
    australia_east = "AustraliaEast"
    australia_southeast = "AustraliaSoutheast"
    brazil_south = "BrazilSouth"
    canada_central = "CanadaCentral"
    canada_east = "CanadaEast"
    west_europe = "WestEurope"
    north_europe = "NorthEurope"
    central_india = "CentralIndia"
    south_india = "SouthIndia"
    west_india = "WestIndia"
    japan_east = "JapanEast"
    japan_west = "JapanWest"
    korea_central = "KoreaCentral"
    korea_south = "KoreaSouth"
    uk_west = "UkWest"
    uk_south = "UkSouth"
    north_central_us = "NorthCentralUs"
    east_us = "EastUs"
    west_us2 = "WestUs2"
    south_central_us = "SouthCentralUs"
    central_us = "CentralUs"
    east_us2 = "EastUs2"
    west_us = "WestUs"
    west_central_us = "WestCentralUs"
    germany_central = "GermanyCentral"
    germany_northeast = "GermanyNortheast"
    china_north = "ChinaNorth"
    china_east = "ChinaEast"

class AzureOfferCode(str, Enum):

    unknown = "Unknown"
    msazr0003_p = "MSAZR0003P"
    msazr0044_p = "MSAZR0044P"
    msazr0059_p = "MSAZR0059P"
    msazr0060_p = "MSAZR0060P"
    msazr0062_p = "MSAZR0062P"
    msazr0063_p = "MSAZR0063P"
    msazr0064_p = "MSAZR0064P"
    msazr0029_p = "MSAZR0029P"
    msazr0022_p = "MSAZR0022P"
    msazr0023_p = "MSAZR0023P"
    msazr0148_p = "MSAZR0148P"
    msazr0025_p = "MSAZR0025P"
    msazr0036_p = "MSAZR0036P"
    msazr0120_p = "MSAZR0120P"
    msazr0121_p = "MSAZR0121P"
    msazr0122_p = "MSAZR0122P"
    msazr0123_p = "MSAZR0123P"
    msazr0124_p = "MSAZR0124P"
    msazr0125_p = "MSAZR0125P"
    msazr0126_p = "MSAZR0126P"
    msazr0127_p = "MSAZR0127P"
    msazr0128_p = "MSAZR0128P"
    msazr0129_p = "MSAZR0129P"
    msazr0130_p = "MSAZR0130P"
    msazr0111_p = "MSAZR0111P"
    msazr0144_p = "MSAZR0144P"
    msazr0149_p = "MSAZR0149P"
    msmcazr0044_p = "MSMCAZR0044P"
    msmcazr0059_p = "MSMCAZR0059P"
    msmcazr0060_p = "MSMCAZR0060P"
    msmcazr0063_p = "MSMCAZR0063P"
    msmcazr0120_p = "MSMCAZR0120P"
    msmcazr0121_p = "MSMCAZR0121P"
    msmcazr0125_p = "MSMCAZR0125P"
    msmcazr0128_p = "MSMCAZR0128P"
    msazrde0003_p = "MSAZRDE0003P"
    msazrde0044_p = "MSAZRDE0044P"

class AzurePricingTier(str, Enum):

    standard = "Standard"
    basic = "Basic"

class AzureStorageRedundancy(str, Enum):

    unknown = "Unknown"
    locally_redundant = "LocallyRedundant"
    zone_redundant = "ZoneRedundant"
    geo_redundant = "GeoRedundant"
    read_access_geo_redundant = "ReadAccessGeoRedundant"

class Percentile(str, Enum):

    percentile50 = "Percentile50"
    percentile90 = "Percentile90"
    percentile95 = "Percentile95"
    percentile99 = "Percentile99"

class TimeRange(str, Enum):

    day = "Day"
    week = "Week"
    month = "Month"

class AssessmentStage(str, Enum):

    in_progress = "InProgress"
    under_review = "UnderReview"
    approved = "Approved"

class Currency(str, Enum):

    unknown = "Unknown"
    usd = "USD"
    dkk = "DKK"
    cad = "CAD"
    idr = "IDR"
    jpy = "JPY"
    krw = "KRW"
    nzd = "NZD"
    nok = "NOK"
    rub = "RUB"
    sar = "SAR"
    zar = "ZAR"
    sek = "SEK"
    try_enum = "TRY"
    gbp = "GBP"
    mxn = "MXN"
    myr = "MYR"
    inr = "INR"
    hkd = "HKD"
    brl = "BRL"
    twd = "TWD"
    eur = "EUR"
    chf = "CHF"
    ars = "ARS"
    aud = "AUD"
    cny = "CNY"

class AzureHybridUseBenefit(str, Enum):

    unknown = "Unknown"
    yes = "Yes"
    no = "No"

class AssessmentSizingCriterion(str, Enum):

    performance_based = "PerformanceBased"
    as_on_premises = "AsOnPremises"

class AssessmentStatus(str, Enum):

    created = "Created"
    updated = "Updated"
    running = "Running"
    completed = "Completed"
    invalid = "Invalid"

class AzureDiskType(str, Enum):

    unknown = "Unknown"
    standard = "Standard"
    premium = "Premium"

class AzureDiskSize(str, Enum):

    unknown = "Unknown"
    standard_s4 = "Standard_S4"
    standard_s6 = "Standard_S6"
    standard_s10 = "Standard_S10"
    standard_s20 = "Standard_S20"
    standard_s30 = "Standard_S30"
    standard_s40 = "Standard_S40"
    standard_s50 = "Standard_S50"
    premium_p4 = "Premium_P4"
    premium_p6 = "Premium_P6"
    premium_p10 = "Premium_P10"
    premium_p20 = "Premium_P20"
    premium_p30 = "Premium_P30"
    premium_p40 = "Premium_P40"
    premium_p50 = "Premium_P50"

class CloudSuitability(str, Enum):

    unknown = "Unknown"
    not_suitable = "NotSuitable"
    suitable = "Suitable"
    conditionally_suitable = "ConditionallySuitable"
    readiness_unknown = "ReadinessUnknown"

class AzureDiskSuitabilityExplanation(str, Enum):

    unknown = "Unknown"
    not_applicable = "NotApplicable"
    disk_size_greater_than_supported = "DiskSizeGreaterThanSupported"
    no_suitable_disk_size_for_iops = "NoSuitableDiskSizeForIops"
    no_suitable_disk_size_for_throughput = "NoSuitableDiskSizeForThroughput"
    no_disk_size_found_in_selected_location = "NoDiskSizeFoundInSelectedLocation"
    no_disk_size_found_for_selected_redundancy = "NoDiskSizeFoundForSelectedRedundancy"
    internal_error_occurred_for_disk_evaluation = "InternalErrorOccurredForDiskEvaluation"

class AzureNetworkAdapterSuitabilityExplanation(str, Enum):

    unknown = "Unknown"
    not_applicable = "NotApplicable"
    internal_error_occured = "InternalErrorOccured"

class AzureVmSize(str, Enum):

    unknown = "Unknown"
    basic_a0 = "Basic_A0"
    basic_a1 = "Basic_A1"
    basic_a2 = "Basic_A2"
    basic_a3 = "Basic_A3"
    basic_a4 = "Basic_A4"
    standard_a0 = "Standard_A0"
    standard_a1 = "Standard_A1"
    standard_a2 = "Standard_A2"
    standard_a3 = "Standard_A3"
    standard_a4 = "Standard_A4"
    standard_a5 = "Standard_A5"
    standard_a6 = "Standard_A6"
    standard_a7 = "Standard_A7"
    standard_a8 = "Standard_A8"
    standard_a9 = "Standard_A9"
    standard_a10 = "Standard_A10"
    standard_a11 = "Standard_A11"
    standard_a1_v2 = "Standard_A1_v2"
    standard_a2_v2 = "Standard_A2_v2"
    standard_a4_v2 = "Standard_A4_v2"
    standard_a8_v2 = "Standard_A8_v2"
    standard_a2m_v2 = "Standard_A2m_v2"
    standard_a4m_v2 = "Standard_A4m_v2"
    standard_a8m_v2 = "Standard_A8m_v2"
    standard_d1 = "Standard_D1"
    standard_d2 = "Standard_D2"
    standard_d3 = "Standard_D3"
    standard_d4 = "Standard_D4"
    standard_d11 = "Standard_D11"
    standard_d12 = "Standard_D12"
    standard_d13 = "Standard_D13"
    standard_d14 = "Standard_D14"
    standard_d1_v2 = "Standard_D1_v2"
    standard_d2_v2 = "Standard_D2_v2"
    standard_d3_v2 = "Standard_D3_v2"
    standard_d4_v2 = "Standard_D4_v2"
    standard_d5_v2 = "Standard_D5_v2"
    standard_d11_v2 = "Standard_D11_v2"
    standard_d12_v2 = "Standard_D12_v2"
    standard_d13_v2 = "Standard_D13_v2"
    standard_d14_v2 = "Standard_D14_v2"
    standard_d15_v2 = "Standard_D15_v2"
    standard_ds1 = "Standard_DS1"
    standard_ds2 = "Standard_DS2"
    standard_ds3 = "Standard_DS3"
    standard_ds4 = "Standard_DS4"
    standard_ds11 = "Standard_DS11"
    standard_ds12 = "Standard_DS12"
    standard_ds13 = "Standard_DS13"
    standard_ds14 = "Standard_DS14"
    standard_ds1_v2 = "Standard_DS1_v2"
    standard_ds2_v2 = "Standard_DS2_v2"
    standard_ds3_v2 = "Standard_DS3_v2"
    standard_ds4_v2 = "Standard_DS4_v2"
    standard_ds5_v2 = "Standard_DS5_v2"
    standard_ds11_v2 = "Standard_DS11_v2"
    standard_ds12_v2 = "Standard_DS12_v2"
    standard_ds13_v2 = "Standard_DS13_v2"
    standard_ds14_v2 = "Standard_DS14_v2"
    standard_ds15_v2 = "Standard_DS15_v2"
    standard_f1 = "Standard_F1"
    standard_f2 = "Standard_F2"
    standard_f4 = "Standard_F4"
    standard_f8 = "Standard_F8"
    standard_f16 = "Standard_F16"
    standard_f1s = "Standard_F1s"
    standard_f2s = "Standard_F2s"
    standard_f4s = "Standard_F4s"
    standard_f8s = "Standard_F8s"
    standard_f16s = "Standard_F16s"
    standard_g1 = "Standard_G1"
    standard_g2 = "Standard_G2"
    standard_g3 = "Standard_G3"
    standard_g4 = "Standard_G4"
    standard_g5 = "Standard_G5"
    standard_gs1 = "Standard_GS1"
    standard_gs2 = "Standard_GS2"
    standard_gs3 = "Standard_GS3"
    standard_gs4 = "Standard_GS4"
    standard_gs5 = "Standard_GS5"
    standard_h8 = "Standard_H8"
    standard_h16 = "Standard_H16"
    standard_h8m = "Standard_H8m"
    standard_h16m = "Standard_H16m"
    standard_h16r = "Standard_H16r"
    standard_h16mr = "Standard_H16mr"
    standard_l4s = "Standard_L4s"
    standard_l8s = "Standard_L8s"
    standard_l16s = "Standard_L16s"
    standard_l32s = "Standard_L32s"

class AzureVmSuitabilityExplanation(str, Enum):

    unknown = "Unknown"
    not_applicable = "NotApplicable"
    guest_operating_system_architecture_not_supported = "GuestOperatingSystemArchitectureNotSupported"
    guest_operating_system_not_supported = "GuestOperatingSystemNotSupported"
    boot_type_not_supported = "BootTypeNotSupported"
    more_disks_than_supported = "MoreDisksThanSupported"
    no_suitable_vm_size_found = "NoSuitableVmSizeFound"
    one_or_more_disks_not_suitable = "OneOrMoreDisksNotSuitable"
    one_or_more_adapters_not_suitable = "OneOrMoreAdaptersNotSuitable"
    internal_error_occured_during_compute_evaluation = "InternalErrorOccuredDuringComputeEvaluation"
    internal_error_occured_during_storage_evaluation = "InternalErrorOccuredDuringStorageEvaluation"
    internal_error_occured_during_network_evaluation = "InternalErrorOccuredDuringNetworkEvaluation"
    no_vm_size_supports_storage_performance = "NoVmSizeSupportsStoragePerformance"
    no_vm_size_supports_network_performance = "NoVmSizeSupportsNetworkPerformance"
    no_vm_size_for_selected_pricing_tier = "NoVmSizeForSelectedPricingTier"
    no_vm_size_for_selected_azure_location = "NoVmSizeForSelectedAzureLocation"
    check_red_hat_linux_version = "CheckRedHatLinuxVersion"
    check_open_suse_linux_version = "CheckOpenSuseLinuxVersion"
    check_windows_server2008_r2_version = "CheckWindowsServer2008R2Version"
    check_cent_os_version = "CheckCentOsVersion"
    check_debian_linux_version = "CheckDebianLinuxVersion"
    check_suse_linux_version = "CheckSuseLinuxVersion"
    check_oracle_linux_version = "CheckOracleLinuxVersion"
    check_ubuntu_linux_version = "CheckUbuntuLinuxVersion"
    check_core_os_linux_version = "CheckCoreOsLinuxVersion"
    windows_server_version_conditionally_supported = "WindowsServerVersionConditionallySupported"
    no_guest_operating_system_conditionally_supported = "NoGuestOperatingSystemConditionallySupported"
    windows_client_versions_conditionally_supported = "WindowsClientVersionsConditionallySupported"
    boot_type_unknown = "BootTypeUnknown"
    guest_operating_system_unknown = "GuestOperatingSystemUnknown"
    windows_server_versions_supported_with_caveat = "WindowsServerVersionsSupportedWithCaveat"
    windows_os_no_longer_under_ms_support = "WindowsOSNoLongerUnderMSSupport"
    endorsed_with_conditions_linux_distributions = "EndorsedWithConditionsLinuxDistributions"
    unendorsed_linux_distributions = "UnendorsedLinuxDistributions"
    no_vm_size_for_standard_pricing_tier = "NoVmSizeForStandardPricingTier"
    no_vm_size_for_basic_pricing_tier = "NoVmSizeForBasicPricingTier"

class NameAvailabilityReason(str, Enum):

    available = "Available"
    invalid = "Invalid"
    already_exists = "AlreadyExists"