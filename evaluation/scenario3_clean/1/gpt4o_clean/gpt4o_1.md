| XML Path | Ontology Property | Entity Class | Related Entity Class | Subject Generation | Join Condition | Datatype | Function Name | Function Output |
|----------|--------------------|---------------|------------------------|--------------------|----------------|----------|----------------|------------------|
| `/entry/id` | `:hasID` | `Procedure` | `Identifier` | `concat('lot-', substring-after(text(), 'licitacionesPerfilContratante/'))` |  | | | |
| `/entry/cac-place-ext:ContractFolderStatus/cbc:ContractFolderID` | `:hasID` | `Lot` | `Identifier` | `concat('lot-', normalize-space(text()))` |  | | | |
| `/entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cbc:Name` | `rdfs:label` | `Lot` |  | `use Lot ID` | `use Lot ID` | `xsd:string` |  |  |
| `/entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cbc:TypeCode` | `:hasProcedureType` | `Procedure` | `skos:Concept` | `use Procedure URI` | `use Procedure URI` | | `map_typecode_to_uri` | `http://publications.europa.eu/resource/authority/procurement-procedure-type/open` |
| `/entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cac:BudgetAmount/cbc:TaxExclusiveAmount` | `schema:amount` | `Lot` |  | `use Lot ID` | `use Lot ID` | `xsd:decimal` |  |  |
| `/entry/cac-place-ext:ContractFolderStatus/cac:LocatedContractingParty/cac:Party/cac:PartyIdentification/cbc:ID` | `:hasID` | `org:Organization` | `Identifier` | `concat('org-', text())` |  | | | |
| `/entry/cac-place-ext:ContractFolderStatus/cac:LocatedContractingParty/cac:Party/cbc:WebsiteURI` | `foaf:homepage` | `org:Organization` |  | `use org ID` | `use org ID` | `xsd:anyURI` |  |  |
| `/entry/cac-place-ext:ContractFolderStatus/cac:TenderResult/cbc:AwardDate` | `:hasAwardDecisionDate` | `LotAwardOutcome` |  | `use Lot ID` | `use Lot ID` | `xsd:date` |  |  |
| `/entry/cac-place-ext:ContractFolderStatus/cac:TenderResult/cbc:ReceivedTenderQuantity` | `:hasReceivedTenders` | `SubmissionStatisticalInformation` |  | `use Lot ID` | `use Lot ID` | `xsd:integer` |  |  |
| `/entry/cac-place-ext:ContractFolderStatus/cac:TenderingProcess/cbc:ProcedureCode` | `:hasProcedureType` | `Procedure` | `skos:Concept` | `use Procedure URI` | `use Procedure URI` | | `map_procedurecode_to_uri` | `http://publications.europa.eu/resource/authority/procurement-procedure-type/open` |
| `/entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cac:RequiredCommodityClassification/cbc:ItemClassificationCode` | `schema:category` | `Lot` |  | `use Lot ID` | `use Lot ID` | `xsd:string` |  |  |
| `/entry/cac-place-ext:ContractFolderStatus/cac:RealizedLocation/cbc:CountrySubentityCode` | `:hasCountryCode` | `Lot` | `skos:Concept` | `use Lot ID` | `use Lot ID` | | `map_nuts_to_country_uri` | `http://publications.europa.eu/resource/authority/country/ESP` |
| `/entry/cac-place-ext:ContractFolderStatus/cac:TenderResult/cac:WinningParty/cac:PartyIdentification/cbc:ID` | `:hasID` | `org:Organization` | `Identifier` | `concat('org-', text())` |  | | | |
| `/entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cac:PlannedPeriod/cbc:DurationMeasure` | `schema:duration` | `Lot` |  | `use Lot ID` | `use Lot ID` | `xsd:duration` |  |  |
| `/entry/cac-place-ext:ContractFolderStatus/cac:TenderingTerms/cac:Language/cbc:ID` | `dcterms:language` | `Procedure` |  | `use Procedure URI` | `use Procedure URI` | `xsd:language` |  |  |
