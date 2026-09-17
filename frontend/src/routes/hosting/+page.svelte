<script>    
import { resolve } from '$app/paths';
import testBanner from '$lib/assets/images/testBanner.png';
</script>

<div class="flex h-screen overflow-hidden">

    <!-- Sidebar: 25% width, scrollable -->
    <aside class="w-[25%] h-full flex flex-col border-r border-gray-200 bg-gray-100">

        <h2 class="text-2xl font-semibold text-gray-900 text-center border-2 border-gray-400 rounded-xl px-4 pt-4 pb-2">
        Sidebar Title
        </h2>

        <ul class="flex-1 overflow-y-auto px-4 pt-3 pb-4 space-y-5">

            <!-- Item 1 -->
            <li>
                <a href="{resolve('/')}" 
                class="flex flex-col items-center justify-center gap-3 rounded-3xl border-3 border-gray-400 bg-white p-3 shadow-sm transition hover:shadow-md hover:border-gray-600 hover:scale-105 focus:outline-none focus:ring-3 focus:ring-blue-500">
                    <p class="text-small text-center font-semibold text-gray-900 sm:text-xl">Title long the text goes here explaining the card content and then more</p>
                    <span class="inline-flex rounded-lg px-2 py-0.5 text-sm font-semibold text-black-700 border-2 border-gray-500 bg-yellow-200 shadow-sm sm:text-base sm:px-7">
                        Status
                    </span>
                    <img
                        src="{testBanner}"
                        alt="Card banner"
                        class="w-full h-300px rounded-lg object-cover"
                    />
                </a>
            </li>

            <!-- Item 2 -->
            <li>
                <a href="{resolve('/')}" 
                class="flex flex-col items-center justify-center gap-3 rounded-3xl border-3 border-gray-400 bg-white p-3 shadow-sm transition hover:shadow-md hover:border-gray-600 hover:scale-105 focus:outline-none focus:ring-3 focus:ring-blue-500">
                    <p class="text-small text-center font-semibold text-gray-900 sm:text-xl">Title Doing Something</p>
                    <span class="inline-flex rounded-lg px-2 py-0.5 text-sm font-semibold text-black-700 border-2 border-gray-500 bg-green-200 shadow-sm sm:text-base sm:px-7">
                        Status
                    </span>
                    <img
                        src="{testBanner}"
                        alt="Card banner"
                        class="w-full h-300px rounded-lg object-cover"
                    />
                </a>
            </li>

            <!-- Item 3 -->
            <li>
                <a href="{resolve('/')}" 
                class="flex flex-col items-center justify-center gap-3 rounded-3xl border-3 border-gray-400 bg-white p-3 shadow-sm transition hover:shadow-md hover:border-gray-600 hover:scale-105 focus:outline-none focus:ring-3 focus:ring-blue-500">
                    <p class="text-small text-center font-semibold text-gray-900 sm:text-xl">Title Doing Something but not longer existing</p>
                    <span class="inline-flex rounded-lg px-2 py-0.5 text-sm font-semibold text-black-700 border-2 border-gray-500 bg-red-200 shadow-sm sm:text-base sm:px-7">
                        Status
                    </span>
                    <img
                        src="{testBanner}"
                        alt="Card banner"
                        class="w-full h-300px rounded-lg object-cover"
                    />
                </a>
            </li>

            <!-- Item 4 -->
            <li>
                <a href="{resolve('/')}" 
                class="flex flex-col items-center justify-center gap-3 rounded-3xl border-3 border-gray-400 bg-white p-3 shadow-sm transition hover:shadow-md hover:border-gray-600 hover:scale-105 focus:outline-none focus:ring-3 focus:ring-blue-500">
                    <p class="text-small text-center font-semibold text-gray-900 sm:text-xl">Title Doing Something but not longer existing</p>
                    <span class="inline-flex rounded-lg px-2 py-0.5 text-sm font-semibold text-black-700 border-2 border-gray-500 bg-red-200 shadow-sm sm:text-base sm:px-7">
                        Status
                    </span>
                    <img
                        src="{testBanner}"
                        alt="Card banner"
                        class="w-full h-300px rounded-lg object-cover"
                    />
                </a>
            </li>

            <!-- Item 5 -->
            <li>
                <a href="{resolve('/')}" 
                class="flex flex-col items-center justify-center gap-3 rounded-3xl border-3 border-gray-400 bg-white p-3 shadow-sm transition hover:shadow-md hover:border-gray-600 hover:scale-105 focus:outline-none focus:ring-3 focus:ring-blue-500">
                    <p class="text-small text-center font-semibold text-gray-900 sm:text-xl">Title Doing Something but not longer existing</p>
                    <span class="inline-flex rounded-lg px-2 py-0.5 text-sm font-semibold text-black-700 border-2 border-gray-500 bg-red-200 shadow-sm sm:text-base sm:px-7">
                        Status
                    </span>
                    <img
                        src="{testBanner}"
                        alt="Card banner"
                        class="w-full h-300px rounded-lg object-cover"
                    />
                </a>
            </li>

        </ul>
        
    </aside>


  <!-- Main content: 75% width -->
  <main class="w-[75%] h-full overflow-y-auto p-6">

    <h2 class="text-3xl font-semibold text-gray-900 text-center mb-4">
      Form Title
    </h2>

    <form class="max-w-4xl mx-auto space-y-4">
        
      <!-- Name -->
      <div>
        <label for="name" class="block text-lg font-medium text-gray-700">Name</label>
        <input
          id="name"
          type="text"
          placeholder="Enter name here..."
          class="mt-1 block w-full rounded-md border-2 border-gray-300 shadow-sm px-3 py-3 text-lg"/>
        <span class="mt-1 block text-right text-sm text-gray-700">
            0/250 characters
        </span>
      </div>

      <!-- Banner Image Upload -->
      <div>
        <label for="banner-upload" class="block text-lg font-medium text-gray-700 mb-1">
            Banner Image
        </label>
        <input
            id="banner-upload"
            type="file"
            accept="image/png, image/jpeg"
            class="block w-full text-lg text-gray-700
            file:mr-4 file:py-4 file:px-6
            file:rounded-md file:border-0
            file:text-lg file:font-medium
            file:bg-indigo-50 file:text-gray-700
            hover:file:bg-indigo-100
            border-2 border-gray-300 rounded-md
            cursor-pointer"
        />
      </div>

      <!-- Description -->
      <div>
        <label for="description" class="block text-lg font-medium text-gray-700">Description</label>
        <textarea
            id="description"
            rows="5"
            placeholder="Enter description here..."
            class="mt-1 block w-full rounded-md border-2 border-gray-300 shadow-sm px-3 py-3 text-lg"
        ></textarea>
        <span class="mt-1 block text-right text-sm text-gray-700">
            0/5000 characters
        </span>
      </div>

      <!-- Co Hosts -->
        <div>
            <label for="cohosts" class="block text-lg font-medium text-gray-700">Co-Hosts</label>
            <div class="mt-1 flex flex-wrap items-center gap-2 w-full rounded-md border-2 border-gray-300 shadow-sm focus-within:border-blue-500 focus-within:ring-1 focus-within:ring-blue-500 px-4 py-3">
                <span class="flex items-center gap-1 bg-blue-50 text-blue-700 text-sm font-medium px-2 py-1 rounded-md">
                    Tag One
                    <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </span>

                <span class="flex items-center gap-1 bg-blue-50 text-blue-700 text-sm font-medium px-2 py-1 rounded-md">
                    Tag Two
                    <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </span>

                <input
                id="cohosts"
                type="text"
                placeholder="Type and press Enter..."
                class="flex-1 min-w-30 text-lg outline-none border-none focus:ring-0 p-0"/>
            </div>
            <span class="mt-1 block text-right text-sm text-gray-700">
                0/10 co-hosts
            </span>
        </div>

        <!-- Category and Type -->
        <div class="flex gap-4">
            <!-- Category -->
            <div class="flex-1">
                <label for="category" class="block text-lg font-medium text-gray-700">Category</label>
                <select
                id="category"
                class="mt-1 block w-full rounded-md border-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-4 py-3 text-lg">
                    <option value="">Select category</option>
                    <option value="option1">Option 1</option>
                    <option value="option2">Option 2</option>
                </select>
            </div>

            <!-- Type -->
            <div class="flex-1">
                <label for="type" class="block text-lg font-medium text-gray-700">Type</label>
                <select
                id="type"
                class="mt-1 block w-full rounded-md border-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-4 py-3 text-lg">
                    <option value="">Select type</option>
                    <option value="option1">Option 1</option>
                    <option value="option2">Option 2</option>
                </select>
            </div>
        </div>

        <!-- Location and Opening Time -->
        <div class="flex gap-4">
            <!-- Location -->
            <div class="flex-1">
                <label for="location" class="block text-lg font-medium text-gray-700">Location</label>
                <select
                id="location"
                class="mt-1 block w-full rounded-md border-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-4 py-3 text-lg">
                    <option value="">Select location</option>
                    <option value="option1">Option 1</option>
                    <option value="option2">Option 2</option>
                </select>
            </div>

            <!-- Opening Time -->
            <div class="flex-1">
                <label for="opening-time" class="block text-lg font-medium text-gray-700">Opening Time</label>
                <select
                id="opening-time"
                class="mt-1 block w-full rounded-md border-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-4 py-3 text-lg">
                    <option value="">Select opening time</option>
                    <option value="option1">Option 1</option>
                    <option value="option2">Option 2</option>
                </select>
            </div>
        </div>

        <!-- Chat Privacy and Join Requirement -->
        <div class="flex gap-4">
            <!-- Chat Privacy -->
            <div class="flex-1">
                <label for="chat-privacy" class="block text-lg font-medium text-gray-700">Chat Privacy</label>
                <select
                id="chat-privacy"
                class="mt-1 block w-full rounded-md border-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-4 py-3 text-lg">
                    <option value="">Select chat privacy</option>
                    <option value="option1">Option 1</option>
                    <option value="option2">Option 2</option>
                </select>
            </div>

            <!-- Join Requirement -->
            <div class="flex-1">
                <label for="join-requirement" class="block text-lg font-medium text-gray-700">Join Requirement</label>
                <select
                id="join-requirement"
                class="mt-1 block w-full rounded-md border-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-4 py-3 text-lg">
                    <option value="">Select join requirement</option>
                    <option value="option1">Option 1</option>
                    <option value="option2">Option 2</option>
                </select>
            </div>
        </div>

        <!-- Members -->
        <div>
            <label for="members" class="block text-lg font-medium text-gray-700">Members</label>
            <div class="mt-1 flex flex-wrap items-center gap-2 w-full rounded-md border-2 border-gray-300 shadow-sm focus-within:border-blue-500 focus-within:ring-1 focus-within:ring-blue-500 px-4 py-3">
                <button type="button" class="bg-blue-50 text-blue-700 text-lg font-medium px-2 py-1 rounded-md hover:bg-blue-100">
                Member One
                </button>

                <button type="button" class="bg-blue-50 text-blue-700 text-lg font-medium px-2 py-1 rounded-md hover:bg-blue-100">
                Member Two
                </button>

                <input
                id="members"
                type="text"
                placeholder=""
                class="flex-1 min-w-30 text-lg outline-none border-none focus:ring-0 p-0"/>
            </div>
            <span class="mt-1 block text-right text-sm text-gray-700">
                0/1000 members
            </span>
        </div>

        <!-- Roles (tags) -->
        <div>
            <label for="roles" class="block text-lg font-medium text-gray-700">Roles</label>
            <div class="mt-1 flex flex-wrap items-center gap-2 w-full rounded-md border-2 border-gray-300 shadow-sm focus-within:border-blue-500 focus-within:ring-1 focus-within:ring-blue-500 px-4 py-3">
                <span class="flex items-center gap-1 bg-blue-50 text-blue-700 text-sm font-medium px-2 py-1 rounded-md">
                    Tag One
                    <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </span>

                <span class="flex items-center gap-1 bg-blue-50 text-blue-700 text-sm font-medium px-2 py-1 rounded-md">
                    Tag Two
                    <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </span>

                <input
                id="roles"
                type="text"
                placeholder="Type and press Enter..."
                class="flex-1 min-w-30 text-lg outline-none border-none focus:ring-0 p-0"/>
            </div>
            <span class="mt-1 block text-right text-sm text-gray-700">
                0/100 roles
            </span>
        </div>

        <!-- Buttons in the end of the form -->
        <div class="flex gap-4">
            <button
                type="submit"
                class="flex-1 rounded-md bg-blue-600 px-10 py-3 text-lg font-medium text-white hover:bg-blue-500">
                Save
            </button>

            <button
                type="button"
                class="flex-1 rounded-md bg-green-600 px-10 py-3 text-lg font-medium text-white hover:bg-green-500">
                Publish
            </button>

            <button
                type="button"
                class="w-32 shrink-0 rounded-md bg-red-600 px-10 py-3 text-lg font-medium text-white hover:bg-red-500">
                Delete
            </button>
        </div>
      

    </form>
  </main>

</div>

<style>

</style>