ScenesToRender: list = ["Start", "Environment", "Reward"]


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
            "end": 'Nun ist es die Aufgabe des "agents" nach diesen Gegebenheiten eine optimale "policy" zu entwerfen, das heißt zu erlernen welche "action" man je nach "state" am besten wählt. Die Besonderheit von "Reinforcement Learning" Problemen ist, dass dem "agent" weder die "Reward-Function", noch die "Transition-Function" bekannt ist. Also muss er durch die Interaktion mit seiner Umgebung lernen. Dabei befindet er sich jedem Schritt in einem neuen "state" und erhält dazu passend einen "reward". Um seinen "reward" zu maximieren, arbeitet der "agent" eine immer bessere "policy" aus.',
        },
        "Praxis-Environment": {
            "agent": "Um euch Schritt für Schritt zu erklären wie alles funktioniert, werden wir uns an einem Beispiel orientieren. Hier unser Szenario:Alles dreht sich um den sogenannten agent. Stellt euch das so vor wie eine Spielfigur in einem Videospiel",
            "title": "Praxis: Environment",
            "start": "In diesem Szenario folgen wir einem Elfen, der versucht, ein Geschenk zu erreichen.",
            "real_start": "Dafür muss er sich über einen zugefrorenen See bewegen, indem er sich wie auf einem Schachbrett von Feld zu Feld bewegt.",
            "show_lake": "Jeder Schritt ist eine sogenannte action. Bei jeder action verändert sich der Zustand des Szenarios. Den nennt man state. Wichtig ist, dass der agent typischerweise kein Vorwissen über die Umgebung hat.",
            "slippery1": "Dabei muss er nicht nur den richtigen Weg finden und die Löcher in der Eisdecke umgehen in dem er die richtige Abfolge von Schritten macht, sondern auch damit umgehen, dass die Eisdecke rutschig ist.",
            "slippery2": "Es kann also passieren, dass er statt in die gewählte Richtung auch in eine andere Richtung rutscht.",
            "transtiton_function": 'Diese Definition von Übergängen zwischen den States nennt man "transition function"',
        },
    }

    @staticmethod
    def get_text(scene_name: str, text_part: str) -> str:
        return Text_Helper.SCENE_TEXTS[scene_name][text_part]
