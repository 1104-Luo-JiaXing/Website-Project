<script>
  //Jeremy Backend testing code, not used in production
  /*import { PUBLIC_API_URL } from '$env/static/public';
  import { onMount } from 'svelte';

  let status = $state('checking...');

  onMount(async () => {
    const res = await fetch(`${PUBLIC_API_URL}/api/health`);
    const data = await res.json();
    status = data.status;
  });*/

  //<p>Backend says: {status}</p> put in the html to display the backend status

  import homeBackground from '$lib/assets/images/home_background.jpg';
  import featureIconOne from '$lib/assets/icons/feature.svg';

</script>

<!-- Main Image-->
<div class="relative w-full h-[60vh] md:h-screen overflow-hidden border-b-5 border-blue-500 -mt-30">
  <!-- Full-Width Image -->
  <img src={homeBackground} alt="background_image" class="absolute inset-0 w-full h-full object-cover"/>
  
  <!-- Centered Text -->
  <div class="absolute inset-0 flex flex-col items-center justify-center bg-black/75 px-4 text-center gap-10">
    <h1 class="text-4xl md:text-7xl font-extrabold text-white">
      Website Project
    </h1>

    <p class="mt-4 text-lg md:text-3xl text-gray-200 max-w-3xl">
      Connect for a unique purpose.
    </p>
  </div>

  <button class="absolute bottom-15 left-1/2 transform -translate-x-1/2 text-lg bg-blue-600 border-3 border-blue-200 hover:bg-blue-900 text-white py-3 px-6 rounded-2xl transition duration-300
  md:text-3xl md:py-6 md:px-12 md:bottom-35">
    Get Started
  </button>

</div>

<!-- Idea Paragraph Section -->
<div class="flex flex-col items-center justify-center px-4 text-center gap-5">
  <h2 class="text-3xl md:text-5xl font-bold text-gray-800 mt-10">
    The Main Idea
  </h2>


  <p class="mt-4 text-lg md:text-2xl text-black max-w-7xl">
    This paragraph will explain the idea of the platform and what it is about. It will provide a brief overview of the platform's purpose, features, and benefits to users. The content will be engaging and informative, encouraging users to explore further and get involved with the platform.
  </p>
</div>

<!-- Feature Section -->
<div class="py-12 max-w-8xl mx-auto px-4">
  <h2 class="text-3xl md:text-5xl font-bold text-gray-800 text-center mb-12">
    Special Features
  </h2>

  <!-- Features -->
  <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8 text-center text-lg border-t-2 border-b-2 border-black p-6">
    
    <!-- Feature 1 -->
    <div class="flex flex-col items-center p-4">
      <img src={featureIconOne} alt="Feature One" class="w-16 h-16 mb-4 scale-150 object-contain" />
      <p class="text-gray-600 text-sm leading-relaxed">
        This is a short paragraph describing the first special feature of the app.
      </p>
    </div>

    <!-- Feature 2 -->
    <div class="flex flex-col items-center p-4">
      <img src={featureIconOne} alt="Feature Two" class="w-16 h-16 mb-4 scale-150 object-contain" />
      <p class="text-gray-600 text-sm leading-relaxed">
        This is a short paragraph describing the second special feature of the app.
      </p>
    </div>

    <!-- Feature 3 -->
    <div class="flex flex-col items-center p-4">
      <img src={featureIconOne} alt="Feature Three" class="w-16 h-16 mb-4 scale-150 object-contain" />
      <p class="text-gray-600 text-sm leading-relaxed">
        This is a short paragraph describing the third special feature of the app.
      </p>
    </div>

  </div>
</div>

<!-- How to use the platform -->
<div class="flex flex-col items-center justify-center px-4 text-center gap-5">
  <h2 class="text-3xl md:text-5xl font-bold text-gray-800 mt-10">
    How to use the platform
  </h2>

  <p class="mt-4 text-lg md:text-2xl text-black max-w-7xl">
    * Show a list of things and ways of how the users can use the platform.
    * A tutorial video will be show in this section to help users understand the platform better.
    * This paragraph will talk about how to use the platform, providing step-by-step instructions or tips for new users and guide users through the process of signing up, navigating the platform.
  </p>
</div>

<!-- Spacer for footer -->
<div class="pb-15"></div>

<style>
  
</style>