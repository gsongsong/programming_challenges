# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard

def append(attack_pattern, beam_strength, num_attack):
    attack_pattern.append([beam_strength, num_attack])
    return beam_strength * num_attack

def get_num_hack(shield_capa, attack_pattern_string):
    # print('--------------------')
    # print('Shield: {0}, Pattern: {1}'.format(shield_capa, attack_pattern_string))
    attack_pattern = []
    damage_total, num_attack_total, beam_strength, num_attack = 0, 0, 1, 0
    for letter in attack_pattern_string:
        if letter == 'S':
            num_attack_total += 1
            num_attack += 1
        elif letter == 'C':
            damage_total += append(attack_pattern, beam_strength, num_attack)
            beam_strength *= 2
            num_attack = 0
    if num_attack_total > shield_capa:
        return 'IMPOSSIBLE'
    if num_attack:
        damage_total += append(attack_pattern, beam_strength, num_attack)
    # print('Pattern: {0}, Total damage: {1}'.format(attack_pattern, damage_total))
    num_hack = 0
    while damage_total > shield_capa:
        deficit = damage_total - shield_capa
        beam_strength, num_attack = attack_pattern[-1]
        beam_half = beam_strength / 2
        num_decr = min(int(deficit / beam_half + 0.5), num_attack)
        damage_decr = beam_half * num_decr
        num_hack += num_decr
        attack_pattern[-1][1] -= num_decr
        attack_pattern[-2][1] += num_decr
        damage_total -= damage_decr
        if not attack_pattern[-1][1]:
            del attack_pattern[-1]
        # print(attack_pattern)
    return num_hack


if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        shield_capa, attack_pattern_string = input().strip().split()
        shield_capa = int(shield_capa)
        num_hack = get_num_hack(shield_capa, attack_pattern_string)
        print('Case #{0}: {1}'.format(i, num_hack))
