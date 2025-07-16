| CSV Column           | Ontology Property | Entity Class | Rel. Entity Class | Subject Generation    | Join Condition | Datatype | Function Name | Function Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `trip_id` | `gtfs:trip` | `gtfs:Trip` | `gtfs:Frequency` | `http://transport.linkeddata.es/trip/{trip_id}` | `trip_id` | string | - | - |
| `start_time` | `gtfs:startTime` | `gtfs:Frequency` | `gtfs:Trip` | `http://transport.linkeddata.es/trip/{trip_id}` | `start_time` | time | `formatTime` | Formatted time in `HH:MM:SS` |
| `end_time` | `gtfs:endTime` | `gtfs:Frequency` | `gtfs:Trip` | `http://transport.linkeddata.es/trip/{trip_id}` | `end_time` | time | `formatTime` | Formatted time in `HH:MM:SS` |
| `headway_secs` | `gtfs:headwaySeconds` | `gtfs:Frequency` | `gtfs:Trip` | `http://transport.linkeddata.es/trip/{trip_id}` | `headway_secs` | integer | - | - |
| `exact_times` | `gtfs:usesExactTimes` | `gtfs:Frequency` | `gtfs:Trip` | `http://transport.linkeddata.es/trip/{trip_id}` | `exact_times` | boolean | `mapExactTimes` | SKOS URI: `/exact-times/frequency` or `/exact-times/schedule` |
| `route_id` | `gtfs:route` | `gtfs:Route` | `gtfs:Trip` | `http://transport.linkeddata.es/route/{route_id}` | `route_id` | string | - | - |
| `service_id` | `gtfs:service` | `gtfs:Service` | `gtfs:Trip` | `http://transport.linkeddata.es/service/{service_id}` | `service_id` | string | - | - |
| `trip_headsign` | `gtfs:headsign` | `gtfs:Trip` | `gtfs:Route` | `http://transport.linkeddata.es/trip/{trip_id}` | `trip_headsign` | string | - | - |
| `trip_short_name` | `gtfs:shortName` | `gtfs:Trip` | `gtfs:Route` | `http://transport.linkeddata.es/trip/{trip_id}` | `trip_short_name` | string | - | - |
| `direction_id` | `gtfs:direction` | `gtfs:Trip` | `gtfs:Route` | `http://transport.linkeddata.es/trip/{trip_id}` | `direction_id` | integer | `mapDirection` | SKOS URI: `/direction/one-direction` or `/direction/opposite-direction` |
| `shape_id` | `gtfs:shape` | `gtfs:Shape` | `gtfs:Trip` | `http://transport.linkeddata.es/shape/{shape_id}` | `shape_id` | string | - | - |
| `wheelchair_accessible` | `gtfs:wheelchairAccessible` | `gtfs:Trip` | `gtfs:Stop` | `http://transport.linkeddata.es/trip/{trip_id}` | `wheelchair_accessible` | integer | `mapWheelchairAccessible` | SKOS URI: `/accesible`, `/inaccesible`, or `/no-information` |
| `agency_id` | `gtfs:agency` | `gtfs:Agency` | `gtfs:Route` | `http://transport.linkeddata.es/agency/{agency_id}` | `agency_id` | string | - | - |
| `route_short_name` | `gtfs:shortName` | `gtfs:Route` | `gtfs:Agency` | `http://transport.linkeddata.es/route/{route_id}` | `route_short_name` | string | - | - |
| `route_long_name` | `gtfs:label` | `gtfs:Route` | `gtfs:Agency` | `http://transport.linkeddata.es/route/{route_id}` | `route_long_name` | string | - | - |
| `route_desc` | `gtfs:description` | `gtfs:Route` | `gtfs:Agency` | `http://transport.linkeddata.es/route/{route_id}` | `route_desc` | string | - | - |
| `route_type` | `gtfs:routeType` | `gtfs:Route` | `gtfs:Agency` | `http://transport.linkeddata.es/route/{route_id}` | `route_type` | integer | - | - |
| `route_url` | `gtfs:url` | `gtfs:Route` | `gtfs:Agency` | `http://transport.linkeddata.es/route/{route_id}` | `route_url` | string | - | - |
| `route_color` | `gtfs:color` | `gtfs:Route` | `gtfs:Agency` | `http://transport.linkeddata.es/route/{route_id}` | `route_color` | string | - | - |
| `route_text_color` | `gtfs:textColor` | `gtfs:Route` | `gtfs:Agency` | `http://transport.linkeddata.es/route/{route_id}` | `route_text_color` | string | - | - |
| `shape_pt_lat` | `geo:lat` | `gtfs:Shape` | `gtfs:Trip` | `http://transport.linkeddata.es/shape/{shape_id}` | `shape_pt_lat` | decimal | - | - |
| `shape_pt_lon` | `geo:long` | `gtfs:Shape` | `gtfs:Trip` | `http://transport.linkeddata.es/shape/{shape_id}` | `shape_pt_lon` | decimal | - | - |
| `shape_pt_sequence` | `gtfs:sequence` | `gtfs:Shape` | `gtfs:Trip` | `http://transport.linkeddata.es/shape/{shape_id}` | `shape_pt_sequence` | integer | - | - |
| `shape_dist_traveled` | `gtfs:distance` | `gtfs:Shape` | `gtfs:Trip` | `http://transport.linkeddata.es/shape/{shape_id}` | `shape_dist_traveled` | decimal | - | - |
| `monday` to `sunday` | `gtfs:{day}` | `gtfs:Service` | `gtfs:Trip` | `http://transport.linkeddata.es/service/{service_id}` | each weekday | boolean | - | - |
| `start_date` | `gtfs:startDate` | `gtfs:Service` | `gtfs:Trip` | `http://transport.linkeddata.es/service/{service_id}` | `start_date` | date | - | - |
| `end_date` | `gtfs:endDate` | `gtfs:Service` | `gtfs:Trip` | `http://transport.linkeddata.es/service/{service_id}` | `end_date` | date | - | - |
| `exception_type` | `gtfs:exceptionType` | `gtfs:Service` | `gtfs:Trip` | `http://transport.linkeddata.es/service/{service_id}` | `exception_type` | integer | - | - |
