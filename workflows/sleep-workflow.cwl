class: Workflow
cwlVersion: v1.0
inputs:
  input0: File
  input1: File
outputs: []
steps:
  task0:
    in:
      input0: input0
    out: [out]
    run:
      baseCommand: sleep 10
      class: CommandLineTool
      hints: {}
      inputs:
        input0: {type: string}
      outputs:
        out: {type: string}
  task1:
    in:
      input1: input1
    out: [out]
    run:
      baseCommand: sleep 10
      class: CommandLineTool
      hints: {}
      inputs:
        input1: {type: string}
      outputs:
        out: {type: string}
  task2:
    in:
      input2: task0/out
    out: [out]
    run:
      baseCommand: sleep 10
      class: CommandLineTool
      hints: {}
      inputs:
        input2: {type: string}
      outputs:
        out: {type: string}
  task3:
    in:
      input3: task0/out
    out: [out]
    run:
      baseCommand: sleep 10
      class: CommandLineTool
      hints: {}
      inputs:
        input3: {type: string}
      outputs:
        out: {type: string}
  task4:
    in:
      input4: task1/out
    out: [out]
    run:
      baseCommand: sleep 10
      class: CommandLineTool
      hints: {}
      inputs:
        input4: {type: string}
      outputs:
        out: {type: string}
  task5:
    in:
      input5: task1/out
    out: [out]
    run:
      baseCommand: sleep 10
      class: CommandLineTool
      hints: {}
      inputs:
        input5: {type: string}
      outputs:
        out: {type: string}
  task6:
    in:
      input6: task2/out
    out: [out]
    run:
      baseCommand: sleep 10
      class: CommandLineTool
      hints: {}
      inputs:
        input6: {type: string}
      outputs:
        out: {type: string}
  task7:
    in:
      input7: task2/out
    out: [out]
    run:
      baseCommand: sleep 10
      class: CommandLineTool
      hints: {}
      inputs:
        input7: {type: string}
      outputs:
        out: {type: string}
  task8:
    in:
      input8_0: task2/out
      input8_1: task4/out
    out: [out]
    run:
      baseCommand: sleep 10
      class: CommandLineTool
      hints: {}
      inputs:
        input8_0: {type: string}
        input8_1: {type: string}
      outputs:
        out: {type: string}
  task9:
    in:
      input9: task5/out
    out: [out]
    run:
      baseCommand: sleep 10
      class: CommandLineTool
      hints: {}
      inputs:
        input9: {type: string}
      outputs:
        out: {type: string}
  task10:
    in:
      input10: task5/out
    out: [out]
    run:
      baseCommand: sleep 10
      class: CommandLineTool
      hints: {}
      inputs:
        input10: {type: string}
      outputs:
        out: {type: string}
  task11:
    in:
      input11: task5/out
    out: [out]
    run:
      baseCommand: sleep 10
      class: CommandLineTool
      hints: {}
      inputs:
        input11: {type: string}
      outputs:
        out: {type: string}
