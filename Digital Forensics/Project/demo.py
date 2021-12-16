import sys

try:
    from jinja2 import Template
except ImportError:
    print("[-] Install required third-party module jinja2")
    sys.exit(1)


DEMO = Template("""type = ['','info','success','warning','danger'];


demo = {
    initPickColor: function(){
        $('.pick-class-label').click(function(){
            var new_class = $(this).attr('new-class');
            var old_class = $('#display-buttons').attr('data-class');
            var display_div = $('#display-buttons');
            if(display_div.length) {
            var display_buttons = display_div.find('.btn');
            display_buttons.removeClass(old_class);
            display_buttons.addClass(new_class);
            display_div.attr('data-class', new_class);
            }
        });
    },

    initChartist: function(){

        var data = {
          labels: [{{bar_labels}}],
          series: [[{{bar_series}}]]
        };

        var options = {
            seriesBarDistance: 10,
            axisX: {
                showGrid: false
            },
            height: "245px"
        };

        var responsiveOptions = [
          ['screen and (max-width: 640px)', {
            seriesBarDistance: 5,
            axisX: {
              labelInterpolationFnc: function (value) {
                return value[0];
              }
            }
          }]
        ];

        Chartist.Bar('#chartActivity', data, options, responsiveOptions);

        var dataPreferences = {
            series: [
                [25, 30, 20, 25]
            ]
        };

        var optionsPreferences = {
            donut: true,
            donutWidth: 40,
            startAngle: 0,
            total: 100,
            showLabel: false,
            axisX: {
                showGrid: false
            }
        };

        Chartist.Pie('#chartPreferences', dataPreferences,
          optionsPreferences);

        Chartist.Pie('#chartPreferences', {
          labels: [{{pi_labels}}],
          series: [{{pi_series}}]
        });

        Chartist.Pie('#chartPreferences2', dataPreferences,
          optionsPreferences);

        Chartist.Pie('#chartPreferences2', {
          labels: [{{pi_2_labels}}],
          series: [{{pi_2_series}}]
        });
    }

}
""")