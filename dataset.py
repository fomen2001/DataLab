import pandas as pd

# Données avec des descriptions de la personnalité
data = {
    "Index": [i+1 for i in range(30)],
    "Chemin_d_acces": [f"images/image{i+1}.jpg" for i in range(30)],
    "Description": [
        "Je suis Jean Dupont, j'ai 30 ans. Je suis une personne dynamique et sociable, toujours prête à relever de nouveaux défis.",
        "Je suis Ali Mohamed, j'ai 45 ans. J'aime aider les autres et je suis un leader naturel dans mon environnement de travail.",
        "Je suis Li Wang, j'ai 25 ans. Très calme et réfléchi, j'aime m'adonner à la lecture et aux voyages pour enrichir ma vision du monde.",
        "Je suis Maria Garcia, j'ai 32 ans. Je suis très créative et j'aime travailler sur des projets artistiques.",
        "Je suis Sarah Levy, j'ai 40 ans. J'apprécie la tranquillité et je suis passionnée par la nature et l'environnement.",
        "Je suis Ahmed Ben Ali, j'ai 36 ans. Toujours curieux et optimiste, je cherche à apporter des solutions aux défis de la vie.",
        "Je suis Zoe Miller, j'ai 28 ans. Sociable et extravertie, j'adore organiser des événements et rencontrer de nouvelles personnes.",
        "Je suis Juan Carlos, j'ai 50 ans. Ma personnalité est plutôt calme, et j'apprécie les discussions profondes avec des amis proches.",
        "Je suis Amina Diallo, j'ai 22 ans. J'aime explorer de nouvelles idées et m'exprimer à travers l'art et la musique.",
        "Je suis Natasha Petrova, j'ai 34 ans. Je suis pragmatique et orientée vers les objectifs, tout en étant attentionnée envers les autres.",
        "Je suis Karim El Saidi, j'ai 29 ans. Passionné de sport, je suis quelqu'un de très énergique et motivé pour atteindre mes objectifs.",
        "Je suis Clara Dupuis, j'ai 26 ans. Introvertie mais très observatrice, j'apprécie les moments de solitude et de réflexion.",
        "Je suis Pedro Garcia, j'ai 33 ans. J'ai un grand sens de l'humour et j'aime apporter de la légèreté dans les situations complexes.",
        "Je suis Mei Lin, j'ai 38 ans. Mon esprit analytique me permet de résoudre des problèmes rapidement et efficacement.",
        "Je suis Omar Hassan, j'ai 42 ans. Très empathique, j'aime écouter les autres et aider dans les moments difficiles.",
        "Je suis Elena Petrova, j'ai 24 ans. Curieuse et enthousiaste, je suis toujours en quête de nouvelles expériences et connaissances.",
        "Je suis Fatoumata Keita, j'ai 31 ans. Je suis une personne optimiste qui aime relever des défis et apprendre de nouvelles compétences.",
        "Je suis David Cohen, j'ai 29 ans. Réfléchi et calme, je prends le temps d'analyser chaque situation avant d'agir.",
        "Je suis Ahmed Fathi, j'ai 44 ans. Très ambitieux, j'aime me fixer des objectifs à long terme et travailler dur pour les atteindre.",
        "Je suis Laura Lopez, j'ai 27 ans. Toujours joyeuse, j'aime apporter de la positivité à ceux qui m'entourent.",
        "Je suis Samuel N’diaye, j'ai 35 ans. Je suis un leader naturel, doté d'une forte volonté d'aider et de guider les autres.",
        "Je suis Olivia Brown, j'ai 39 ans. Passionnée de voyage, je suis une personne curieuse qui cherche constamment à découvrir de nouvelles cultures.",
        "Je suis Mohamed Al Farsi, j'ai 33 ans. Discret mais intelligent, je préfère observer avant de prendre la parole dans un groupe.",
        "Je suis Jessica White, j'ai 32 ans. Je suis passionnée par la mode et le design, et j'aime m'exprimer à travers ma créativité.",
        "Je suis Naima Zahra, j'ai 28 ans. Très sociable, j'adore organiser des événements pour rassembler les gens autour de causes communes.",
        "Je suis Zaid Ibrahim, j'ai 40 ans. J'ai un caractère réfléchi, ce qui me permet de prendre des décisions judicieuses dans des moments critiques.",
        "Je suis Lucy Scott, j'ai 31 ans. J'aime la simplicité et je trouve du bonheur dans les petites choses de la vie.",
        "Je suis Peter O'Neil, j'ai 55 ans. Avec l'expérience, je suis devenu plus calme et sage, toujours prêt à partager des conseils avisés.",
        "Je suis Aliyah Abdallah, j'ai 27 ans. J'aime discuter de questions sociales et je m'engage activement dans des causes qui me tiennent à cœur.",
        "Je suis Sofia Rios, j'ai 36 ans. Je suis une personne positive et généreuse, toujours prête à soutenir mes amis et ma famille."
    ]
}

# Création du DataFrame
df = pd.DataFrame(data)

# Affichage des 5 premières lignes
print(df.head())
