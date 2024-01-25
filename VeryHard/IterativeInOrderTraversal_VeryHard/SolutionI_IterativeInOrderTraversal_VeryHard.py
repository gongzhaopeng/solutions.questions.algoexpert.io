def iterativeInOrderTraversal(tree, callback):
    dir_from = 0  # from parent
    cur_node = tree
    while True:
        if dir_from == 0:
            if cur_node.left:
                cur_node = cur_node.left
            else:
                dir_from = 1  # from left child
            continue
        elif dir_from == 1:
            callback(cur_node)
            if cur_node.right:
                cur_node = cur_node.right
                dir_from = 0
                continue
        parent = cur_node.parent
        if not parent:
            break
        dir_from = 1 if parent.left is cur_node else 2
        cur_node = parent
