<!DOCTYPE html>
<html lang="en">
<head>
  <title>terribly tiny tales</title>

  <link rel="stylesheet" type="text/css" href="css/util.css">
  <link rel="stylesheet" type="text/css" href="css/main.css?version=17">

  <meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
  <!--===============================================================================================-->
  	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
  <!--===============================================================================================-->
  	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
  <!--===============================================================================================-->
  	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
  <!--===============================================================================================-->
  	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
  <!--===============================================================================================-->
  	<link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
</head>

<body>
  <div class="limiter">
		<div class="container-table100">
			<div class="wrap-table100">
				<div class="table100 ver3 m-b-110">
					<div class="table100-head">
						<table>
							<thead>
								<tr class="row100 head">
									<th class="cell100 column1">Word</th>
									<th class="cell100 column2">Frequency</th>
								</tr>
							</thead>
						</table>
					</div>

					<div class="table100-body js-pscroll">
						<table>
							<tbody>

                <?php
                $number = $_POST["text"];
                $number = (int)$number;

                require "init.php";

                // 1.0 Fetch file from server
                // (already feteched once)
                // file_put_contents("test.txt", file_get_contents("http://terriblytinytales.com/test.txt"));

                // 2.0 Read data from file
                $filecontents = file_get_contents("test.txt");
                $words = preg_split('/[\s]+/', $filecontents, -1, PREG_SPLIT_NO_EMPTY);

                // 3.0 Compute frequency distribution

                // 3.1 generate a set of unique words
                $unique_words = array_unique($words);

                // 3.2 loop through each word in array once
                foreach($unique_words as $i => $item) {
                    $word = $item;
                    $count = 0;

                    // 3.3 find the count for each word in the document
                    foreach ($words as $j => $value) {
                        if (strcmp($word, $value)==0) {
                          $count = $count + 1;
                        }
                    }

                    /*
                    3.4 SQL Query for inserting each word and its count into the database.
                    (already inserted once)
                    $query = "insert into test(word,count) values('".$word."','".$count."');" ;
                    $result = odbc_exec($con,$query);
                    */
                }


                // 4.0 fetch results from database
                $query = "SELECT * FROM dbo.Athletes ORDER BY Name DESC LIMIT $number;";
                $result = odbc_exec($con,$query);

                while ($row = odbc_result_all($result)) {

                  echo "
                  <tr class='row100 body'>
                  <td class='cell100 column1'>" . $row['Name'] . "</td>
                  <td class='cell100 column2'>" . $row['Description'] . "</td>
                  </tr>";
                }
                odbc_close($con);
                ?>

                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>


    <!--===============================================================================================-->
  	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
    <!--===============================================================================================-->
    <script src="vendor/bootstrap/js/popper.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>
    <!--===============================================================================================-->
    <script src="vendor/select2/select2.min.js"></script>
    <!--===============================================================================================-->
    <script src="vendor/perfect-scrollbar/perfect-scrollbar.min.js"></script>
    <script>
    	$('.js-pscroll').each(function(){
    		var ps = new PerfectScrollbar(this);

    		$(window).on('resize', function(){
    			ps.update();
    		})
    	});
    </script>

    <script src="js/main.js"></script>
    <!--===============================================================================================-->

    <script src="//static.codepen.io/assets/common/stopExecutionOnTimeout-b2a7b3fe212eaa732349046d8416e00a9dec26eb7fd347590fbced3ab38af52e.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <script src="https://static.tumblr.com/maopbtg/oimmiw86r/jquery.autosize-min.js"></script>

    <script>
        $(document).ready(function(){
          $('#title').focus();
          $('#text').autosize();
        });
    </script>

</body>
</html>
