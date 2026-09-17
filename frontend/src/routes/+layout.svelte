<script>
	import favicon from '$lib/assets/favicon.svg';
	import '../app.css';
	import { resolve } from '$app/paths';
	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>


<nav class="navbar flex flex-row fixed items-stretch bg-gray-100 text-black justify-between rounded-3xl top-2 left-5 right-5 z-50 
font-medium border-3 border-gray-600 outline-10 outline-gray-300 text-base p-3 md:text-xl md:p-5">
	<!-- Most left Side-->
	<a href={resolve('/')} class="w-20 sm:w-24 text-base md:text-xl">Logo</a>

	<div class="flex flex-row justify-center items-stretch flex-1 gap-x-4 md:gap-7 text-base md:text-xl">
		<a href={resolve('/')} class = "hover:scale-125 hover:transition-transform hover:duration-100 hover:text-blue-800 hover:bg-blue-200 hover:px-3 hover:rounded-2xl ">Home</a>
		<a href={resolve('/search')} class = "hover:scale-125 hover:transition-transform hover:duration-100 hover:text-blue-800 hover:bg-blue-200 hover:px-3 hover:rounded-2xl">Search</a>
		<a href={resolve('/saved')} class = "hover:scale-125 hover:transition-transform hover:duration-100 hover:text-blue-800 hover:bg-blue-200 hover:px-3 hover:rounded-2xl">Saved</a>
		<a href={resolve('/inbox')} class = "hover:scale-125 hover:transition-transform hover:duration-100 hover:text-blue-800 hover:bg-blue-200 hover:px-3 hover:rounded-2xl">Inbox</a>
		<a href={resolve('/hosting')} class = "hover:scale-125 hover:transition-transform hover:duration-100 hover:text-blue-800 hover:bg-blue-200 hover:px-3 hover:rounded-2xl">Hosting</a>
	</div>

	<!-- Most right Side-->
	<a href={resolve('/')} class="w-20 sm:w-24 text-right text-base md:text-xl">Login</a>
</nav>

<!-- Spacer for making room for the fixed navbar -->
<div class="h-20 sm:h-28"></div>

{@render children()}

<footer class="mt-auto w-full bg-gray-200 text-black p-5 border-t-5 border-gray-500"> &copy; 2026 Website-Project. All rights reserved. </footer>
