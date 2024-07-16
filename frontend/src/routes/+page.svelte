<script lang="ts">
	let name = '';
	let data: {};
</script>

<h1>Concurrently HMR</h1>

<h2>Normal Endpoint</h2>

<p>Fill in the input and press the 'Say Hello' button:</p>

<label for="name">Input:</label>
<input id="name" type="text" bind:value={name} />

<button
	on:click={async () => {
		const response = await fetch(`http://localhost:8100/hello?name=${name}`);
		console.log('response', response);
		data = await response.json();
		console.log('data', data);
	}}
>
	Say Hello
</button>

<p>Output: {JSON.stringify(data)}</p>

<h2>Exception Endpoint</h2>

<p>Press the button to throw a backend exception:</p>

<button on:click={() => fetch('http://localhost:8100/goodbye')}>Throw Exception</button>

<button on:click={() => fetch('http://localhost:8100/async_goodbye')}>Throw Async Exception</button>
