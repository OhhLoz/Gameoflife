#                                                                   Static Components

block         = [[1, 1],#   █ █
                 [1, 1]]#   █ █

beehive       = [[0, 1, 1, 0],#       █ █
                 [1, 0, 0, 1],#     █     █
                 [0, 1, 1, 0]]#       █ █

loaf          = [[0, 1, 1, 0],#       █ █
                 [1, 0, 0, 1],#     █     █
                 [0, 1, 0, 1],#       █   █
                 [0, 0, 1, 0]]#         █

boat          = [[1, 1, 0],#        █ █
                 [1, 0, 1],#        █   █
                 [0, 1, 0]]#          █

tub           = [[0, 1, 0],#          █
                 [1, 0, 1],#        █   █
                 [0, 1, 0]]#          █

#                                                                   Oscillators

blinker = [1, 1, 1]#        █ █ █

toad    = [[1, 1, 1, 0],#   █ █ █
           [0, 1, 1, 1]]#     █ █ █

beacon  = [[1, 1, 0, 0],#     █ █
           [1, 0, 0, 0],#     █
           [0, 0, 0, 1],#           █
           [0, 0, 1, 1]]#         █ █

pulsar  =  [[0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],#    █ █ █      █ █ █
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],# █        █  █       █
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],# █        █  █       █
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],# █        █  █       █
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],#    █ █ █      █ █ █
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],#    █ █ █      █ █ █
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],# █        █  █       █
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],# █        █  █       █
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],# █        █  █       █
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]]#    █ █ █      █ █ █

pentadecathlon = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0],#     █         █
                  [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],# █ █   █ █ █ █   █ █
                  [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]]#     █         █


#                                                                   Spaceships

glider = [[1, 0, 0],# █
          [0, 1, 1],#   █ █
          [1, 1, 0]]# █ █

lwss = [[0, 1, 0, 0, 1],#   █     █
        [1, 0, 0, 0, 0],# █
        [1, 0, 0, 0, 1],# █       █
        [1, 1, 1, 1, 0]]# █ █ █ █

mwss = [[0, 0, 0, 1, 0, 0],#      █
        [0, 1, 0, 0, 0, 1],#   █       █
        [1, 0, 0, 0, 0, 0],# █
        [1, 0, 0, 0, 0, 1],# █         █
        [1, 1, 1, 1, 1, 0]]# █ █ █ █ █

hwss = [[0, 0, 0, 1, 1, 0, 0],#      █ █
        [0, 1, 0, 0, 0, 0, 1],#   █         █
        [1, 0, 0, 0, 0, 0, 0],# █
        [1, 0, 0, 0, 0, 0, 1],# █           █
        [1, 1, 1, 1, 1, 1, 0]]# █ █ █ █ █ █

#                                                                   Methuselahs

rpentomino = [[0, 1, 1],#   █ █
              [1, 1, 0],# █ █
              [0, 1, 0]]#   █

diehard = [[0, 0, 0, 0, 0, 0, 1, 0],#             █
           [1, 1, 0, 0, 0, 0, 0, 0],# █ █
           [0, 1, 0, 0, 0, 1, 1, 1]]#   █       █ █ █

acorn =   [[0, 1, 0, 0, 0, 0, 0],#   █
           [0, 0, 0, 1, 0, 0, 0],#       █
           [1, 1, 0, 0, 1, 1, 1]]# █ █     █ █ █

#                                                                   Miscellaneous

gosperglidergun = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                   [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                   [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

                   #                                                 █
                   #                                             █   █
                   #                         █ █             █ █                         █ █
                   #                       █       █         █ █                         █ █
                   # █ █                 █           █       █ █
                   # █ █                 █       █   █ █         █   █
                   #                     █           █               █
                   #                       █       █
                   #                         █ █

blockswitchengine   = [[0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 1, 0, 1, 1],
                       [0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0, 0, 0]]


#                                                                   Infinite Growth

#https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life