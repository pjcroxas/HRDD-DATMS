def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls', '.pptx', '']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')
    limit = 2 * 2500 * 2500
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 12 MiB.')

#      // $.ajax({
# // url:'{% url 'ticketing-dashboard' %}',
# // type: 'GET',
# // success: function (response){
# //   $('#tabs').html(response['html'])
# //   test1 = response['jsonget'];
# //     alert(test1)
# //       // var=response_json.variable_value; #Here I always get the same in every minutes despite the variable get new value in every minute in the view.
# //    },
# //
# //  });
