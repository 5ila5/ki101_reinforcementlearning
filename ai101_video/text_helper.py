ScenesToRender: list = [
    "Start",
    "Environment",
    "Reward",
    "QTable",
    "Training",
    "Explore_Exploite",
    "Abschluss",
]


class Text_Helper:
    SCENE_TEXTS: dict[str, dict] = {
        "Start": {
            "title": "Reinforcement learning",
            "start_1": "Haben Sie sich jemals gefragt, wie ein selbstfahrendes Auto lernt sich fortzubewegen",
            "start_2": "oder wie Schachprogramme ihre eigene Strategie mit der Zeit verbessern? Das ist die beeindruckende Fähigkeit des Reinforcement Learnings, einem Teilgebiet der künstlichen Intelligenz.",
            "start_3": "Der entscheidende Vorteil dieser Variante ist, dass es dadurch möglich wird, Systeme zu entwerfen, die sich durch die Interaktion mit ihrem Umfeld kontinuierlich verbessern und sich so an verschiedenste Szenarien anpassen können. Doch wie lässt sich so etwas umsetzen?",
        },
        "Reward": {
            "title": "Reward-Function",
            "start": 'Zuletzt bleibt noch die sogenannte "Reward-Function"',
            "rewards": 'Damit unser "agent" weiß, welchen Übergang er am besten verwenden soll, wird jedem "state" in unserem Szenario ein positiver oder negativer "reward" zugeordnet, also entweder eine Belohnung oder eine Bestrafung, je nachdem, ob der "state" hilfreich oder schädlich für das zu erreichende Ziel ist.',
            "elf_rewarded": "In unserem Szenario erhält der  Elf dann eine Belohnung, wenn er es geschafft hat das Geschenk zu erreichen,",
            "elf_not_rewarded": " ansonsten geht er leer aus.",
            "markov": "Zusammengenommen bezeichnet man diese Art von Problemstellung als Markov Decision Process (MDP) nach Andrej Markov.",
            "policy_1": 'Nun ist es die Aufgabe des "agents" nach diesen Gegebenheiten eine optimale "policy" zu entwerfen. ',
            "policy_2": 'Aber was ist eine Policy. Über eine Policy erlernt der "agent" welche "action" in einem "state" am besten zu wählen ist. Die Besonderheit von "Reinforcement Learning" Problemen ist, dass dem "agent" weder die "Reward-Function", noch die "Transition-Function" bekannt ist. Also muss er durch die Interaktion mit seiner Umgebung lernen. Dabei befindet er sich jedem Schritt in einem neuen "state" und erhält dazu passend einen "reward". Um seinen "reward" zu maximieren, arbeitet der "agent" eine immer bessere "policy" aus.',
            "question_mark": "?",
            "arrow_text": "findet",
            "policy_text_1": "optimale policy",
            "policy_text_2": "Policy",
        },
        "Praxis-Environment": {
            "title": "Praxis: Environment",
            "agent": "Um euch Schritt für Schritt zu erklären wie alles funktioniert, werden wir uns an einem Beispiel orientieren. Hier unser Szenario: Alles dreht sich um den sogenannten agent. Stellt euch das so vor wie eine Spielfigur in einem Videospiel",
            "start": "In diesem Szenario folgen wir einem Elfen, der versucht, ein Geschenk zu erreichen.",
            "real_start": "Dafür muss er sich über einen zugefrorenen See bewegen, indem er sich wie auf einem Schachbrett von Feld zu Feld bewegt.",
            "show_lake": "Jeder Schritt ist eine sogenannte action. Bei jeder action verändert sich der Zustand des Szenarios. Den nennt man state. Wichtig ist, dass der agent typischerweise kein Vorwissen über die Umgebung hat.",
            "slippery1": "Dabei muss er nicht nur den richtigen Weg finden und die Löcher in der Eisdecke umgehen in dem er die richtige Abfolge von Schritten macht, sondern auch damit umgehen, dass die Eisdecke rutschig ist.",
            "slippery2": "Es kann also passieren, dass er statt in die gewählte Richtung auch in eine andere Richtung rutscht.",
            "transtiton_function": 'Diese Definition von Übergängen zwischen den States nennt man "transition function"',
        },
        "QTabble": {
            "title": "Q-Tabelle",
            "start": "Unser Elf arbeitet dafür mit einer Q-Tabelle. Die ist praktisch das Gehirn des Elfs. Jede Zeile steht hier für ein Feld in unserer Welt. "
            "Dort wird die Bewertung von jedem Feld nach dem Lernprozess gespeichert",
            "richtig": "und so kann der Elf je nach Wert entscheiden, welcher Zug der beste in der aktuellen Situation ist. "
            #  'Hier wird nicht nur der direkte "reward"  eines "states" beachtet, sondern auch die "rewards", die sich zukünftig von diesem "state" aus erreichbar sind. '
            #  'Diese werden je nach der Anzahl der benötigten "actions" um einen bestimmten Faktor abgeschwächt, damit die direkten "rewards" weiterhin eine wichtige Rolle spielen.',
        },
        "Training": {
            "start": "Schauen wir uns jetzt einmal an, wie ein solcher Trainingsdurchlauf funktioniert:",
            "active_1": 'Zu Beginn des Trainings gibt es in der Q-Tabelle noch keinerlei Präferenzen für die Züge, weil er noch kein Wissen über die Umgebung und seine besten "actions" hat und verhält sich daher zunächst zufällig, da er  so möglichst viel Information über die "rewards" der jeweiligen Situation sammeln kann.',
            "active_2": 'Dieser Ansatz wird als "active learning" bezeichnet, da der "agent" aktiv Entscheidungen trifft und dann basierend auf den "rewards" lernt.',
            "passive": 'Alternativ kann man auch "passive learning" verwenden. Dabei fungiert der "agent" eher als Beobachter und verhält sich nach einer vorgegebenen "policy", um Informationen über die Umgebung zu sammeln.',
            "active_text_title": "Active Learning",
            "active_text_1": "Agent trifft aktiv",
            "active_text_2": "auf den Rewards",
            "active_text_3": "Entscheidungen basierend",
            "passive_text_title": "Passive Learning",
            "passive_text": "Agent fungiert als Beobachter",
        },
        "Explore_Exploite": {
            "title": "Der Exploration vs. Exploitation tradeoff",
            "title_voice_text": "Im Training für Reinforcement Learning Agenten gibt es ein fundamentales Dilemma: Der Exploration vs. Exploitation tradeoff.",
            "explore": "Exploration bezeichnet dabei das Erkunden der Umgebung unabhängig von der Policy, damit bessere Ansätze auch dann gefunden werden, wenn sie stark von den aktuellen Daten abweichen.",
            "exploite": "Wendet man Exploitation an, so folgt man streng der aktuell besten policy, da das der beste aktuell bekannte Weg ist.",
            "end": 'Beides ist notwendig, da Exploitation das Optimum möglicherweise verfehlt und Exploration zu ungerichtet ist, um in sinnvoller Zeit Ergebnisse zu erzielen. Hier wird dieses Problem durch die "exploration decay rate" gelöst. Diese legt die Wahrscheinlichkeit fest mit der der Agent von der aktuellen policy abweicht um Exploration anzuwenden. Diese wird mit der Zeit immer kleiner, sodass man sich immer mehr auf das Gefundene verlässt.',
            "explore_title": "Exploration",
            "explore_text_1": "Von der aktuellen Policy abweichen",
            "explore_text_2": "Erkunden, um neue Wege zu finden",
            "exploite_title": "Exploitation",
            "exploite_text_1": "Die aktuelle Policy befolgen",
            "exploite_text_2": "Die besten bekannten Wege nutzen",
            "tradeoff_title": "Tradeoff",
            "tradeoff_explore_text": "Geht in uninteressante Richtungen",
            "tradeoff_exploite_text": "Beginnt Umwege zu gehen",
            "decay_rate_title": "Lösung: Exploration decay rate",
            "decay_rate_text_1": "Mit welcher Wahrscheinlichkeit",
            "decay_rate_text_2": "der Agent exploriert",
            "decay_rate_text_3": "Wird mit der Zeit immer kleiner",
        },
        "End": {
            "title": "Abschlusssatz zu Neural-Networks",
            "NN": "Abschließend wollen wir noch erwähnen, dass es sich bei unserem Ansatz mit der Q-Tabelle natürlich nur um einzelnen Ansatz in einem großen Feld handelt. Man kann natürlich viele andere Varianten, wie beispielsweise neurale Netze, die die Neuronen-Struktur eines Gehirns nachahmen sollen, verwenden und vieles mehr. Das alles würde aber den Rahmen dieses kurzen Videos sprengen.",
            "ending": "Wir hoffen, dass wir einen guten Einblick geben  und für die nächste Begegnung mit Reinforcement Learning ein wenig Licht ins Dunkel bringen konnten und laden dazu ein. sich bei Interesse den beigelegten Code für das gezeigte Szenario anzuschauen. Vielen Dank fürs Zuschauen!",
            "ending_text": "Vielen Dank fürs Zuschauen!",
        },
    }

    @staticmethod
    def get_text(scene_name: str, text_part: str) -> str:
        return Text_Helper.SCENE_TEXTS[scene_name][text_part]
