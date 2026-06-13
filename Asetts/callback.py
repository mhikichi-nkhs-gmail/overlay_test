"""
Replicator COMP Callbacks

me - this DAT
"""

from typing import Any, List

def onReplicate(comp, allOps, newOps, template, master):
    table = op('fish_table')

    # パート1：パラメータをテーブルから流し込む
    for c in newOps:
        if table.cell(c.name, 'id') is None:
            continue
        c.par.Period = float(table.cell(c.name, 'Period').val)
        c.par.Amplitude = float(table.cell(c.name, 'Amplitude').val)
        c.par.Yamp = float(table.cell(c.name, 'Yamp').val)
        c.par.Ycenter = float(table.cell(c.name, 'Ycenter').val)
        c.par.Yseed = int(table.cell(c.name, 'Yseed').val)
        c.par.Yperiod = int(table.cell(c.name, 'Yperiod').val)
        c.par.Scale = float(table.cell(c.name, 'Scale').val)
        c.par.Phaseoffset = float(table.cell(c.name, 'Phaseoffset').val)
        c.par.Escape = float(table.cell(c.name, 'Escape').val)
        c.par.Sensitivity = float(table.cell(c.name, 'Sensitivity').val)
        # Ycenter があれば追加
        if table.cell(c.name, 'Ycenter') is not None:
            c.par.Ycenter = float(table.cell(c.name, 'Ycenter').val)

    # パート2：Composite TOP に再接続
    composite = op('/project1/composite1')
    if composite is None:
        return

    for conn in composite.inputConnectors:
        if conn.connections:
            conn.disconnect()

    for i, c in enumerate(allOps):
        if i >= len(composite.inputConnectors):
            break
        c.outputConnectors[0].connect(composite.inputConnectors[i])

    return


def onRemoveReplicant(comp, replicant):
    replicant.destroy()
    return