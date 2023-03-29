class TMConfig:

    title = u'Développement d’un site interactif pour l’apprentissage de l’arithmétique modulaire'
    first_name = 'Louis-Guillaume'
    last_name = 'Fanton'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Avril'
    seminary_title = u'Développement Web'
    tutor = u"Cédric Donner et Johan Jobin"
    release = "Version intermédiaire"
    repository_url = "https://github.com/Oheir"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

tmconfig = TMConfig()