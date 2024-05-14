'''

written by Emily Pollacchi
  	file name alignX
  	Copyright (C) 2024 by Emily Pollacchi
  	epollacchi@gmail.com

'''

import maya.cmds as cmds

def alignX():
    # Select objects
    selObjs = cmds.ls(selection=True)

    # Check for selection
    if not selObjs:
        cmds.error("No objects selected.")

    # Move pivot to the bottom
    for Objs in selObjs:
        bbox = cmds.exactWorldBoundingBox(Objs)
        bottom = [(bbox[0] + bbox[3]) / 2, bbox[1], (bbox[2] + bbox[5]) / 2]
        cmds.xform(Objs, piv=bottom, ws=True)

    # Move object to the origin
    for Objs in selObjs:
        cmds.move(0, 0, 0, Objs, rpr=True, absolute=True)

    # Freeze transformations
    for Objs in selObjs:
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

    # Move objects along the X axis. You can change 5 to another number to change the spacing.
    inc = 0
    for Objs in selObjs:
        cmds.move(inc * 5, 0, 0, Objs)
        inc = inc + 1

    # Freeze transformations
    for Objs in selObjs:
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

    # Delete non-deformer history
    for Objs in selObjs:
        cmds.BakeNonDefHistory()


alignX()