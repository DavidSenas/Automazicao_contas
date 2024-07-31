def Pegando_Estados(estado):
    Estado = estado
    Sigla_Estado = ""
    Lista_Estados = {"AL": "Alabama", "AK": "Alaska", "AR": "Arkansas", "AZ": "Arizona", "CA": "California",
                     "KS": "Kansas", "NC": "North Carolina",
                     "SC": "South Carolina", "CO": "Colorado", "CT": "Connecticut", "ND": "North Dakota",
                     "SD": "South Dakota",
                     "DE": "Delaware", "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
                     "RI": "Rhode Island",
                     "IL": "Illinois", "IN": "Indiana", "IA": "Iow", "KY": "Kentucky", "LA": "Louisiania",
                     "ME": "Maine",
                     "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
                     "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire",
                     "NJ": "New Jersey", "NY": "New York", "NM": "New México", "OK": "Oklahoma", "OH": "Ohio",
                     "OR": "Oregon", "PA": "Pennsylvania", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
                     "VT": "Vermont", "VA": "Virginia", "WV": "West Virginia", "WA": "Washington",
                     "WI": "Wisconsin", "WY": "Wyoming"}

    for siglas, estados in Lista_Estados.items():
        if estados == Estado:
            Sigla_Estado = siglas

            print(Estado)
            return siglas