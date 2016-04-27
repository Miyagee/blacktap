<div data-value="1839471" class="numCounter">
          <b></b><span>,</span><b></b><b></b><b></b><span>,</span><b></b><b></b><b></b>
        </div>

    <script type="text/javascript">
        function Counter(selector) {
          this.el = $(selector);
          this.numbers = this.el.find('> b').toArray().reverse();
        }

        Counter.prototype.count = function(newVal) {
          var reversedArr, className;
          // update instance's value
          this.value = newVal || this.el.attr('data-value') | 0;

          if (!this.value) return;
          // convert value into an array of numbers
          reversedArr = (this.value + '').split('').reverse();
          // loop on each number element and change it
          this.numbers.forEach(function(item, i) {
            setTimeout(function() {
              className = 'd' + reversedArr[i] || 0;
              //if( item.className != className)
              item.className = className;
            }, i * 250);
          })
        }

        /////////////// create new counter for this demo ///////////////////////

        var counter = new Counter('.numCounter');
        displayCount();

        function displayCount() {
            counter.count(<?php include 'php/odometer_data.php' ?>);
        }
    </script>