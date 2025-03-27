
def segundos_para_hhmmss(tempo_em_segundos, verbose=False):

    tempo_em_segundos = int(6000)
    hh = tempo_em_segundos // 3600
    mm = (tempo_em_segundos % 3600) // 60
    ss = tempo_em_segundos % 60

    if verbose:
        print(f"{hh}: {mm}: {ss}")

    return
segundos_para_hhmmss (tempo_em_segundos, verbose=True)