class TMConfig:

    title = u'Développement d’un site interactif pour l’apprentissage de l’arithmétique modulaire'
    first_name = 'Louis-Guillaume'
    last_name = 'Fanton'
    address = u"Chemin de la Reraise 46, 1616 Attalens"
    author = f'{first_name} {last_name}'
    the_date = f"Le 30 mars 2023"
    year = u'2023'
    month = u'Avril'
    seminary_title = u'Développement Web'
    tutor = u"Cédric Donner et Johan Jobin"
    release = ""
    repository_url = "https://github.com/Oheir"
    

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

tmconfig = TMConfig()