$(function() {
  $('#select-server').on('change', function(e) {
    e.preventDefault();
    if($(this).val()==='')
      return false;
    $.post('/floweditor/getScenarios/',$('#fileform').serialize(),function(data) {
      if(data.scenarios.length>0) {
        var select = $('select[name="scenario"]');
        select.html("<option value=''>-------</option>");
        for(var s in data.scenarios) {
          select.append('<option>'+data.scenarios[s]+'</option>');
        }
      }
    },'json');
  });

  $('#select-scenario').on('change', function(e) {
    e.preventDefault();
    if($(this).val()==='')
      return false;
    $.post('/floweditor/getScenarioFlows/',$('#fileform').serialize(),function(data) {
      if(data.flows.length>0) {
        var select = $('select[name="flow"]');
        select.html("<option value=''>-------</option>");
        for(var s in data.flows) {
          select.append('<option>'+data.flows[s]+'</option>');
        }
      }
    },'json');
  });

  $(document.body).on('change','#select-flow', function(e) {
    if($('#select-flow').val()==='')
      return false;
    e.preventDefault();
    $.post('/floweditor/getFlowFiles/',$('#fileform').serialize() ,function(data) {
      if(data.files.length>0) {
        var flows = $('#file_list');
        flows.html("");
        for(var s in data.files) {
          flows.append('<li><a class="flowlink">'+data.files[s]+'</a></li>');
        }
      }
    },'json');
  });

  $(document.body).on('click','#file_list li a', function(e) {
    e.preventDefault();
    document.current_file = $(this).text();
    $('#filename').text($(this).text());
    $.post('/floweditor/getFlowFileContent/',$('#fileform').serialize()+'&file='+$(this).text() ,function(data) {
      $('#filecontent').html(data.file_content);
      document.editor.setValue(data.file_content);
    },'json');
  });

  $(document.body).on('click','.downloadScenario',function(e) {
    e.preventDefault();
    $('#fileform').attr('action','/floweditor/downloadScenarioZip/');
    $('#fileform').attr('target','_blank');
    $('#fileform').submit();

  });

  $(document.body).on('click','#save_file', function(e) {
    e.preventDefault();
    var new_content = document.editor.getValue();
    $.post('/floweditor/saveFlowFileContent/',$('#fileform').serialize()+'&file='+document.current_file+'&file_content='+encodeURIComponent(new_content) ,function(data) {
      //$('#filecontent').html(data.file_content);
    },'json');
  });

  document.editor = CodeMirror.fromTextArea($('#filecontent')[0], {
    lineNumbers: true,
    mode: {name:"xml",htmlMode: false},
    viewportMargin: Infinity
  });
});