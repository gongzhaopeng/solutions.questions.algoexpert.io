def waterfallStreams(array, source):
    pre_streams = array[0].copy()
    pre_streams[source] = 100
    cur_streams = array[len(array) - 1]
    for floor_index in range(1, len(array) - 1):
        floor = array[floor_index]
        right_flow_stream = 0
        pre_outlet = -1
        left_blocked = True
        pre_floor = array[floor_index - 1]
        for grid_index, down_blocked in enumerate(floor):
            if pre_floor[grid_index]:
                left_blocked = True
                right_flow_stream = 0
            if not down_blocked:
                cur_streams[grid_index] = right_flow_stream + pre_streams[grid_index]
                right_flow_stream = 0
                pre_outlet = grid_index
                if not pre_floor[grid_index]:
                    left_blocked = False
            elif pre_streams[grid_index]:
                halved = pre_streams[grid_index] / 2
                if not left_blocked and pre_outlet > -1:
                    cur_streams[pre_outlet] += halved
                right_flow_stream += halved
        pre_streams, cur_streams = cur_streams, pre_streams
        for i in range(len(cur_streams)):
            cur_streams[i] = 0
    return pre_streams
