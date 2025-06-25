class SensorController:
    @staticmethod
    def avaliar(presenca=False, luminosidade=0, temperatura=0):
        acoes = []
        if presenca:
            acoes.append("⚠️ Alarme ativado: movimento detectado!")
        if luminosidade > 80:
            acoes.append("💡 Luz apagada: ambiente claro.")
        if temperatura > 50:
            acoes.append("🚨 Sirene acionada: alta temperatura!")
        return acoes
