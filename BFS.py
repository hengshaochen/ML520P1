#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Heng-Shao Cnen
'''
import sys
import Start
import Queue
class BFS(object):
    # 初始化迷宫大小和密度
    def __init__(self):
        self.node_to_go = {}
        self.node_has_been = dict()
        self.size = -1
        #self.density = density
        #self.map_matrix = []
        #for i in range(size):
        #    self.map_matrix.append([])
        #    for j in range(size):
        #        self.map_matrix[i].append(0)

    #DFS遍历
    def bfs_init(self, map, size):
        #start point
        self.node_to_go = {}
        self.node_has_been = dict()
        self.size = size
        start_node = (0, 0)
        end_node = (size - 1, size - 1)
        self.bfs(map, start_node, end_node)

    def bfs(self, map, start_node, end_node):
        q = Queue.Queue()
        q.put(start_node)
        self.node_has_been[start_node] = (-1, -1)
        map[start_node[0]][start_node[1]] = 1

        deltaX = [0, 1, -1, 0]
        deltaY = [1, 0, 0, -1]

        distance_traveled = 0
        while not q.empty():
            distance_traveled += 1
            currentQSize = q.qsize()
            for i in range(0, currentQSize):
                currentNode = q.get()
                for j in range(0, 4):
                    neighborNode = (currentNode[0] + deltaX[j], currentNode[1] + deltaY[j])

                    if neighborNode[0] < 0 or neighborNode[1] < 0 or neighborNode[1] \
                                    >= self.size or neighborNode[0] >= self.size:
                        continue

                    if neighborNode == end_node:
                        self.node_has_been[neighborNode] = currentNode
                        #for (k, v) in self.node_has_been.items():
                        #    print k
                        #    print v
                        #    print "--"
                            # print path
                        target = end_node
                        while (target != start_node):
                            print target
                            for (k,v) in self.node_has_been.items():
                                if k == target:
                                    buf = self.node_has_been.get(k)
                                    target = buf
                                    break
                        print start_node

                        # print distance
                        print "distance:"
                        print distance_traveled
                        return
                    if not map[neighborNode[0]][neighborNode[1]]:
                        self.node_has_been[neighborNode] = currentNode
                        map[neighborNode[0]][neighborNode[1]] = 1
                        q.put(neighborNode)
        print "not distance"

if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    # set the size and density of this matrix
    size = 4
    start = Start.Start(size, 0.2)
    start.print_matrix()
    start.paint_random()
    start.print_matrix()
    bfs = BFS()
    bfs.bfs_init(start.get_matrix(), size)