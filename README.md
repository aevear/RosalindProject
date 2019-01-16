<!-- Rosalind-->
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>

<div style="border-top:5px solid silver; border-bottom: 5px solid silver; text-align: center; padding-top: 20px; padding-bottom: 5px;">
  <h1>Rosalind Project</h1>
</div>
<div style="padding-top: 20px; padding-bottom: 5px;">
  <p>
    The Rosalind Project started right after I had finished with my Bacheors in Biology. I had decidede after taking to some of my teachers in school during my last semster that I wanted to study more computer science and ultimlately study Bioinformatics (which I ended up doing the following year).
  </p>
  <p>
    I ended up completing quite a large amount of them during this time period and learned a lot of the basics of coding and programming by doing these tasks. During my masters courses I did not end up making many more of these as most of my time was utilized by the school. However, during my internship at Pharmacelera I learned a lot more about good coding practices and redesigned each of the code bits for use in a library that could eventually be downloaded by any one attempting to preform the tasks listed in Rosalind.
  </p>
  <p>
    So now, I will explain how the project is broken down, what else needs to be done and how to use the codes found here!
  </p>
  <h2>Project Breakdown</h2>
  <h3>Overview</h3>
  <p>
    The project is broken into two major parts on the top most level, the input files and the source code. The input files is where you can store all the inputs that you are given and where the code will pull data from to complete tasks. If you need it to be used in another way you can feel free to message me or you can attempt to modify it yourself, its not too complex of an input system.
  </p>
  <h3>Source Code</h3>
  <p>
    The code mainly functions in a way similar to the way that the deepchem library functions, the only library that I have spent a large amount of time becoming familiar with. It has a root call function called runLib that can be called and contains a full list of all of the individual problems that I have had to deal with. This file is only used if you want to use the library and not include it in another larger system.
  </p>
  <h3>Rosalind Library</h3>
  <p>
    This is the meat of the code and contains the problem code, the tool code and the loader code (There may be more sections included later if I end up needing them).
  </p>
  <p>
    The problem codes are each written to solve a single problem found at rosalind and are called when using the runLib code. These in turn pull from their own code, tool and loader code.
  </p>
  <p>
    Loader is primarily a single bit of code that takes the import data and sends it to the program in a usable format, specifically in a list of list. (I will eventually move this to an object but it is not nessesary at the moment).
  </p>
  <p>
    The tool code is primarly functons that I have used in more than one code and can easily be reused in new code. As more progress is made on this library this section will expand quite a bit more.
  </p>
  <!--



  __________________________________________



  -->

  <h2>More Resources</h2>
  <h4> <a href="https://github.com/aevear/RosalindProject">Github link</a></h4>

<!--



__________________________________________



-->

  <h2>Rosalind Problem Tutorials</h2>

  <table style="width:100%; border: 0;">

  <tr> <!-- Title-->
    <th>
    </th>
  </tr>

  <!--New Section in Table-->
  <tr>
    <th width="8%">
    </th>
    <th>
      <ul>
       <li style="font-weight:normal">DNA: Counting DNA Nucleotides</li>
      </ul>
    </th>
    <th>
      <a href="http://xanhahn.me/rosalind-dna/"><span class="glyphicon glyphicon-link"></span></a>
    </th>
  </tr>

  <!--New Section in Table-->
  <tr>
    <th width="8%">
    </th>
    <th>
      <ul>
       <li style="font-weight:normal">RNA: Transcribing DNA into RNA</li>
      </ul>
    </th>
    <th>
      <a href="http://xanhahn.me/rosalind-rna/"><span class="glyphicon glyphicon-link"></span></a>
    </th>
  </tr>

  <!--New Section in Table-->
  <tr>
    <th width="8%">
    </th>
    <th>
      <ul>
       <li style="font-weight:normal">REVC: Complementing a Strand of DNA</li>
      </ul>
    </th>
    <th>
      <a href="http://xanhahn.me/rosalind-dna/"><span class="glyphicon glyphicon-link"></span></a>
    </th>
  </tr>

  <!--New Section in Table-->
  <tr>
    <th width="8%">
    </th>
    <th>
      <ul>
       <li style="font-weight:normal">Counting DNA Nucleotides</li>
      </ul>
    </th>
    <th>
      <a href="http://xanhahn.me/rosalind-revc/"><span class="glyphicon glyphicon-link"></span></a>
    </th>
  </tr>

  <!--New Section in Table-->
  <tr>
    <th width="8%">
    </th>
    <th>
      <ul>
       <li style="font-weight:normal">FIB: Rabbits and Recurrence Relations</li>
      </ul>
    </th>
    <th>
      <a href="http://xanhahn.me/rosalind-fib/"><span class="glyphicon glyphicon-link"></span></a>
    </th>
  </tr>

  <!--New Section in Table-->
  <tr>
    <th width="8%">
    </th>
    <th>
      <ul>
       <li style="font-weight:normal">GC: Computing GC Content </li>
      </ul>
    </th>
    <th>
      <a href="http://xanhahn.me/rosalind-gc/"><span class="glyphicon glyphicon-link"></span></a>
    </th>
  </tr>

  <!--New Section in Table-->
  <tr>
    <th width="8%">
    </th>
    <th>
      <ul>
       <li style="font-weight:normal">Hamm: Counting Point Mutations </li>
      </ul>
    </th>
    <th>
      <a href="http://xanhahn.me/rosalind-hamm/"><span class="glyphicon glyphicon-link"></span></a>
    </th>
  </tr>

  <!--New Section in Table-->
  <tr>
    <th width="8%">
    </th>
    <th>
      <ul>
       <li style="font-weight:normal">IPRB: Mendel's First Law </li>
      </ul>
    </th>
    <th>
      <a href="http://xanhahn.me/rosalind-iprb/"><span class="glyphicon glyphicon-link"></span></a>
    </th>
  </tr>

  <!--New Section in Table-->
  <tr>
    <th width="8%">
    </th>
    <th>
      <ul>
       <li style="font-weight:normal">Subs: Finding a Motif in DNA</li>
      </ul>
    </th>
    <th>
      <a href="http://xanhahn.me/rosalind-subs/"><span class="glyphicon glyphicon-link"></span></a>
    </th>
  </tr>

</table>


</div>
