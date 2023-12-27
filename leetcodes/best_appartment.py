"""algorithim only works when all the reqs are in a block otherwise it gets caught in a infinite loop"""

def can_reach(num, req):
    if not -1 < num < len(blocks):
        return False
    if blocks[num][req]:
        return True
    return False

blocks = [
    {
        'gym': False,
        'school': True,
        'store': True,
    }, 
    {
        'gym': True,
        'school': False,
        'store': False,
    },
    {
        'gym': True,
        'school': True,
        'store': False,
    },
    {
        'gym': False,
        'school': True,
        'store': False,
    }
]   

def eval_block(block_num):
    cur_block_farthest = 0
    for req in reqs:
        blocks_needed_to_walk = 0
        while not (can_reach(block_num + blocks_needed_to_walk, req) or can_reach(block_num - blocks_needed_to_walk, req)):
            blocks_needed_to_walk += 1
            if blocks_needed_to_walk == closest_so_far:
                return 
        cur_block_farthest = max(cur_block_farthest, blocks_needed_to_walk)
    if cur_block_farthest < closest_so_far:
        closest_so_far = cur_block_farthest
        closest_block_num = block_num

reqs = ['gym', 'school', 'store']

closest_block_num = -1
closest_so_far = len(blocks)
for block_num in range(len(blocks)):
    eval_block(block_num)
    

absolute_closest = closest_so_far
print(f'{absolute_closest = } {closest_block_num = }')