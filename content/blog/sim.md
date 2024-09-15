+++
title = "Testy symulatora"
description = "Test wbudowanego symulatora"
draft = true
+++


# Działanie bramek logicznych
{% comment() %}
A tu boczny komentarz
{% end %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<div class="example_row">
    <div class="example_button_column" style="width: 40%">
        <button class="example_button" id="or_example_input_a">Zmień stan górnego wejścia</button>
        <button class="example_button" id="or_example_input_b">Zmień stan dolnego wejścia</button>
    </div>
    <div class="example_canvas_wrapper" id="or_example_wrapper" style="width: 60%">
        <canvas class="example_canvas" id="or_example"> 
            Tu powinien być interaktywny przykład bramki OR
        </canvas>
    </div>
</div>
<script type="module" src="./or_sim.js"></script>

<br>

<div class="example_row">
    <div class="example_button_column" style="width: 40%">
        <button class="example_button" id="and_example_input_a">Zmień stan górnego wejścia</button>
        <button class="example_button" id="and_example_input_b">Zmień stan dolnego wejścia</button>
    </div>
    <div class="example_canvas_wrapper" id="and_example_wrapper" style="width: 60%">
        <canvas class="example_canvas" id="and_example"> 
            Tu powinien być interaktywny przykład bramki AND
        </canvas>
    </div>
</div>
<script type="module" src="./and_sim.js"></script>

<br>

<div class="example_row">
    <div class="example_button_column" style="width: 40%">
        <button class="example_button" id="xor_example_input_a">Zmień stan górnego wejścia</button>
        <button class="example_button" id="xor_example_input_b">Zmień stan dolnego wejścia</button>
    </div>
    <div class="example_canvas_wrapper" id="xor_example_wrapper" style="width: 60%">
        <canvas class="example_canvas" id="xor_example"> 
            Tu powinien być interaktywny przykład bramki XOR
        </canvas>
    </div>
</div>
<script type="module" src="./xor_sim.js"></script>