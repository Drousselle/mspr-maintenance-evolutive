from api.models import Espace, Chantier, Tache, Institution, Horaire, Pays, Region, Departement, Arrondissement, Lampadaire

def dummy_generate_chantier():
    espaces = [
        {'id': 'PLC_PIGALLE', 'nom': 'Place Pigalle', 'adresse': 'Place Pigalle 75009 PARIS', 'taches': [
            {'nom': 'Terrassement', 'etat': 'Terminée', 'date_fin': '1986-02-16'},
            {'nom': 'Expertise circulation', 'etat': 'En cours', 'date_fin': '1998-02-16'},
            {'nom': 'Installation sapin de Noël', 'etat': 'Terminée', 'date_fin': '1986-02-16'}
        ]},
        {'id': 'PRC_MONCEAU', 'nom': 'Parc Monceau', 'adresse': '35 Boulevard de Courcelles, 75008 Paris', 'taches': [
            {'nom': 'Pose isolant mousse', 'etat': 'Terminée', 'date_fin': '1977-02-16'},
            {'nom': 'Toitures kiosques', 'etat': 'Terminée', 'date_fin': '1977-02-16'}
        ]},
        {'id': 'RUE_PELC', 'nom': 'Rue piétonne du Poil-au-con', 'adresse': 'Rue du Pélican 75001 PARIS', 'taches': [
            {'nom': 'Terrassement', 'etat': 'Terminée', 'date_fin': '1995-02-1'},
            {'nom': 'Réfection pavés', 'etat': 'Terminée', 'date_fin': '1999-08-10'},
        ]},
        {'id': 'SLL_Z', 'nom': 'Salle Z', 'adresse': 'Plaque Télécom, Port Royal 74014 PARIS', 'taches': [
            {'nom': 'Déblaiement', 'etat': 'Terminée', 'date_fin': '1960-02-16'},
            {'nom': 'Évacuation caddies', 'etat': 'Terminée', 'date_fin': '2009-06-11'},
            {'nom': 'Évacuation caddies', 'etat': 'Terminée', 'date_fin': '2001-11-10'},
            {'nom': 'Évacuation caddies', 'etat': 'Terminée', 'date_fin': '2002-07-03'},
        ]}
    ]

    for espace in espaces:
        taches = espace.pop('taches')
        espace_id = Espace.objects.create(**espace)
        chantier_id = Chantier.objects.create(espace=espace_id)
        for tache in taches:
            Tache.objects.create(**{**tache, **{'chantier': chantier_id}})

def dummy_generate_institution():
    institutions =  [
        {'code': 'POSTE_CHATELET', 'horaires': [
            {'debut': '09:00', 'fin': '17:00'}
        ]},
        {'code': 'POSTE_ARRAS', 'horaires': [
            {'debut': '09:00', 'fin': '12:00'},
            {'debut': '13:00', 'fin': '18:00'}
        ]},
    ]

    for institution in institutions:
        horaires = institution.pop('horaires')
        institution_id = Institution.objects.create(**institution)
        for horaire in horaires:
            Horaire.objects.create(**{**horaire, **{'institution_id': institution_id}})

def dummy_generate_eclairage():
    eclairages = [
        {'code': 'FR', 'regions': [
            {'code': 'IdF', 'departements': [
                {'code': 'PARIS', 'arrondissements': [
                    {'code': '01', 'lampadaires': [
                        {'id': 'CD0X+32', 'latitude': -5.1, 'longitude': -68.3},
                    ]},
                    {'code': '02', 'lampadaires': []},
                    {'code': '03', 'lampadaires': []},
                    {'code': '04', 'lampadaires': [
                        {'id': 'CM1P-t2', 'latitude': -5.1, 'longitude': -68.3},
                        {'id': 'AT43+V2', 'latitude': -23.1, 'longitude': 8.8},
                    ]},
                    {'code': '05', 'lampadaires': []},
                    {'code': '06', 'lampadaires': []},
                    {'code': '07', 'lampadaires': [
                        {'id': 'B3GH-CD', 'latitude': -6.1, 'longitude': -78.3},
                        {'id': 'AOP9+E4', 'latitude': 7.03, 'longitude': -16.84},
                    ]},
                    {'code': '08', 'lampadaires': []},
                    {'code': '09', 'lampadaires': []},
                    {'code': '10', 'lampadaires': []},
                    {'code': '11', 'lampadaires': []},
                    {'code': '12', 'lampadaires': [
                        {'id': 'MM9F-32', 'latitude': 9.8, 'longitude': 8.3},
                    ]},
                    {'code': '13', 'lampadaires': []},
                    {'code': '14', 'lampadaires': []},
                    {'code': '15', 'lampadaires': []},
                    {'code': '16', 'lampadaires': []},
                    {'code': '17', 'lampadaires': []},
                    {'code': '18', 'lampadaires': []},
                    {'code': '19', 'lampadaires': []},
                    {'code': '20', 'lampadaires': []},
                ]}
            ]}
        ]}
    ]
    
    for eclairage in eclairages:
        regions = eclairage.pop('regions')
        pays_id = Pays.objects.create(**eclairage)
        for region in regions:
            departements = region.pop('departements')
            region_id = Region.objects.create(**{**region, **{'pays_id': pays_id}})
            for departement in departements:
                arrondissements = departement.pop('arrondissements')
                dep_id = Departement.objects.create(**{**departement, **{'region_id': region_id}})
                for arrondissement in arrondissements:
                    lampadaires = arrondissement.pop('lampadaires')
                    arrondissement_id = Arrondissement.objects.create(**{**arrondissement, **{'departement_id': dep_id}})
                    for lampadaire in lampadaires:
                        Lampadaire.objects.create(**{**lampadaire, **{'arrondissement_id': arrondissement_id}})

def run():
    dummy_generate_eclairage() # BASED
    dummy_generate_institution() # PORTE
    dummy_generate_chantier() # SEDATIF
