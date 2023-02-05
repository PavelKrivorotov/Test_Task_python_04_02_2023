

DEFAULT_URL = "https://spacex-production.up.railway.app/"

DEFAULT_QUERY_PARAMS = """
query ExampleQuery {
    missions {
        id
        name
        description
    }
    rockets {
        id
        name
        country
        company
        type
    }
    launches {
        id
        details
        mission_name
        mission_id
        rocket {
            rocket {
                id
            }
        }
    }
}
"""