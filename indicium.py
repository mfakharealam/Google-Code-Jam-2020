import itertools


def check_diagonal_sums(mat, nt, kt):
    d_sum = 0
    for i in range(0, nt):
        d_sum += mat[i][i]
    if d_sum == kt:
        return True


def make_combs(size):
    all_list = [[x for x in range(1, size + 1)]] * size
    res = list(itertools.product(*all_list))
    valid_comb = []
    for each in res:
        if len(set(each)) == size:
            valid_comb.append(each)
    return valid_comb


def make_k_comb(li, size, kt):
    for i in range(size):
        tmp_li = li[i:size + i]
        print(tmp_li)
        if check_diagonal_sums(tmp_li, size, kt):
            return tmp_li


tc = int(input())
tmp_tc = tc
while tmp_tc > 0:
    get_in = input().split(" ")
    n = int(get_in[0])
    k = int(get_in[1])
    comb_list = make_combs(n)
    ans = make_k_comb(comb_list, n, k)
    print(ans)
    tmp_tc -= 1

